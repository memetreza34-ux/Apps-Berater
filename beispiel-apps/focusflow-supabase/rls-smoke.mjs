#!/usr/bin/env node

"use strict";

const required = [
  "SUPABASE_URL",
  "SUPABASE_ANON_KEY",
  "USER_A_EMAIL",
  "USER_A_PASSWORD",
  "USER_B_EMAIL",
  "USER_B_PASSWORD",
];

for (const key of required) {
  if (!process.env[key]) {
    console.error(`FEHLER: Umgebungsvariable ${key} fehlt.`);
    process.exit(2);
  }
}

const baseUrl = process.env.SUPABASE_URL.replace(/\/$/, "");
const anonKey = process.env.SUPABASE_ANON_KEY;

async function parseResponse(response) {
  const text = await response.text();
  let body = null;
  if (text) {
    try {
      body = JSON.parse(text);
    } catch {
      body = text;
    }
  }
  if (!response.ok) {
    throw new Error(`${response.status} ${response.statusText}: ${typeof body === "string" ? body : JSON.stringify(body)}`);
  }
  return body;
}

async function signIn(email, password) {
  const response = await fetch(`${baseUrl}/auth/v1/token?grant_type=password`, {
    method: "POST",
    headers: {
      apikey: anonKey,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });
  const body = await parseResponse(response);
  if (!body?.access_token || !body?.user?.id) {
    throw new Error(`Login für ${email} lieferte keine gültige Session.`);
  }
  return { token: body.access_token, userId: body.user.id };
}

async function rest(path, token, options = {}) {
  const headers = {
    apikey: anonKey,
    Authorization: `Bearer ${token}`,
    Accept: "application/json",
    ...options.headers,
  };
  if (options.body !== undefined) {
    headers["Content-Type"] = "application/json";
  }
  const response = await fetch(`${baseUrl}/rest/v1/${path}`, {
    ...options,
    headers,
    body: options.body === undefined ? undefined : JSON.stringify(options.body),
  });
  return parseResponse(response);
}

function assert(condition, message) {
  if (!condition) throw new Error(`ASSERTION FEHLGESCHLAGEN: ${message}`);
}

function pass(message) {
  console.log(`PASS: ${message}`);
}

let projectId = null;
let userA = null;

try {
  userA = await signIn(process.env.USER_A_EMAIL, process.env.USER_A_PASSWORD);
  const userB = await signIn(process.env.USER_B_EMAIL, process.env.USER_B_PASSWORD);
  assert(userA.userId !== userB.userId, "Testkonten müssen unterschiedliche Nutzer sein.");

  const marker = `RLS smoke ${new Date().toISOString()}`;
  const created = await rest("projects?select=id,title,user_id", userA.token, {
    method: "POST",
    headers: { Prefer: "return=representation" },
    body: { title: marker },
  });
  assert(Array.isArray(created) && created.length === 1, "Nutzer A muss genau ein Projekt erstellen können.");
  projectId = created[0].id;
  assert(created[0].user_id === userA.userId, "user_id muss serverseitig Nutzer A entsprechen.");

  const ownRead = await rest(`projects?id=eq.${projectId}&select=id,title,user_id`, userA.token);
  assert(Array.isArray(ownRead) && ownRead.length === 1, "Nutzer A muss eigenes Projekt lesen können.");
  pass("Nutzer A kann eigenes Projekt erstellen und lesen.");

  const foreignRead = await rest(`projects?id=eq.${projectId}&select=id,title,user_id`, userB.token);
  assert(Array.isArray(foreignRead) && foreignRead.length === 0, "Nutzer B darf Projekt von A nicht lesen.");
  pass("Nutzer B kann Projekt von A nicht lesen.");

  const foreignUpdate = await rest(`projects?id=eq.${projectId}&select=id,title`, userB.token, {
    method: "PATCH",
    headers: { Prefer: "return=representation" },
    body: { title: "UNERLAUBTE AENDERUNG" },
  });
  assert(Array.isArray(foreignUpdate) && foreignUpdate.length === 0, "Nutzer B darf Projekt von A nicht ändern.");

  const unchanged = await rest(`projects?id=eq.${projectId}&select=id,title`, userA.token);
  assert(unchanged[0]?.title === marker, "Projekt muss nach fremdem Update unverändert sein.");
  pass("Nutzer B kann Projekt von A nicht ändern.");

  const foreignDelete = await rest(`projects?id=eq.${projectId}&select=id`, userB.token, {
    method: "DELETE",
    headers: { Prefer: "return=representation" },
  });
  assert(Array.isArray(foreignDelete) && foreignDelete.length === 0, "Nutzer B darf Projekt von A nicht löschen.");

  const stillExists = await rest(`projects?id=eq.${projectId}&select=id`, userA.token);
  assert(Array.isArray(stillExists) && stillExists.length === 1, "Projekt muss nach fremdem Delete weiter existieren.");
  pass("Nutzer B kann Projekt von A nicht löschen.");

  const cleanup = await rest(`projects?id=eq.${projectId}&select=id`, userA.token, {
    method: "DELETE",
    headers: { Prefer: "return=representation" },
  });
  assert(Array.isArray(cleanup) && cleanup.length === 1, "Nutzer A muss Testprojekt löschen können.");
  projectId = null;
  pass("Nutzer A kann Testprojekt löschen.");

  console.log("ERFOLG: RLS-Smoke-Test vollständig bestanden.");
} catch (error) {
  console.error(`FEHLER: ${error instanceof Error ? error.message : String(error)}`);

  if (projectId && userA?.token) {
    try {
      await rest(`projects?id=eq.${projectId}`, userA.token, {
        method: "DELETE",
        headers: { Prefer: "return=minimal" },
      });
    } catch {
      console.error("WARNUNG: Automatische Bereinigung des Testprojekts ist fehlgeschlagen.");
    }
  }
  process.exit(1);
}

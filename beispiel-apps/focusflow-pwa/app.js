"use strict";

const STORAGE_KEY = "focusflow-reference-v1";
const SESSION_SECONDS = 25 * 60;

const elements = {
  form: document.querySelector("#task-form"),
  title: document.querySelector("#task-title"),
  error: document.querySelector("#task-error"),
  list: document.querySelector("#task-list"),
  empty: document.querySelector("#empty-state"),
  taskCount: document.querySelector("#task-count"),
  selectedTask: document.querySelector("#selected-task"),
  timer: document.querySelector("#timer"),
  timerState: document.querySelector("#timer-state"),
  startPause: document.querySelector("#start-pause"),
  resetTimer: document.querySelector("#reset-timer"),
  completedCount: document.querySelector("#completed-count"),
  sessionCount: document.querySelector("#session-count"),
  exportData: document.querySelector("#export-data"),
  deleteData: document.querySelector("#delete-data"),
  appStatus: document.querySelector("#app-status"),
};

const initialState = () => ({
  tasks: [],
  selectedTaskId: null,
  secondsRemaining: SESSION_SECONDS,
  completedSessions: 0,
  updatedAt: new Date().toISOString(),
});

let state = loadState();
let timerHandle = null;
let statusTimeout = null;

function loadState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return initialState();
    const parsed = JSON.parse(raw);
    return {
      ...initialState(),
      ...parsed,
      tasks: Array.isArray(parsed.tasks) ? parsed.tasks : [],
      secondsRemaining: Number.isFinite(parsed.secondsRemaining)
        ? Math.max(0, parsed.secondsRemaining)
        : SESSION_SECONDS,
    };
  } catch (error) {
    console.warn("Lokale Daten konnten nicht geladen werden.", error);
    queueMicrotask(() => showStatus("Lokale Daten waren beschädigt und wurden zurückgesetzt."));
    return initialState();
  }
}

function saveState() {
  state.updatedAt = new Date().toISOString();
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch (error) {
    console.error("Lokale Daten konnten nicht gespeichert werden.", error);
    showStatus("Speichern fehlgeschlagen. Prüfe den verfügbaren Browserspeicher.");
  }
}

function createId() {
  if (globalThis.crypto?.randomUUID) return globalThis.crypto.randomUUID();
  return `task-${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function sanitizeTitle(value) {
  return value.trim().replace(/\s+/g, " ");
}

function addTask(title) {
  const task = {
    id: createId(),
    title,
    completed: false,
    createdAt: new Date().toISOString(),
    completedAt: null,
  };
  state.tasks.unshift(task);
  state.selectedTaskId = task.id;
  state.secondsRemaining = SESSION_SECONDS;
  saveState();
  render();
  showStatus(`Aufgabe „${title}“ wurde hinzugefügt und ausgewählt.`);
}

function toggleTask(taskId) {
  const task = state.tasks.find((item) => item.id === taskId);
  if (!task) return;
  task.completed = !task.completed;
  task.completedAt = task.completed ? new Date().toISOString() : null;
  if (task.completed && state.selectedTaskId === task.id) {
    stopTimer();
  }
  saveState();
  render();
  showStatus(task.completed ? "Aufgabe abgeschlossen." : "Aufgabe wieder geöffnet.");
}

function selectTask(taskId) {
  const task = state.tasks.find((item) => item.id === taskId && !item.completed);
  if (!task) return;
  stopTimer();
  state.selectedTaskId = task.id;
  state.secondsRemaining = SESSION_SECONDS;
  saveState();
  render();
  showStatus(`„${task.title}“ ist jetzt ausgewählt.`);
}

function deleteTask(taskId) {
  const task = state.tasks.find((item) => item.id === taskId);
  if (!task) return;
  const accepted = window.confirm(`Aufgabe „${task.title}“ wirklich löschen?`);
  if (!accepted) return;
  state.tasks = state.tasks.filter((item) => item.id !== taskId);
  if (state.selectedTaskId === taskId) {
    stopTimer();
    state.selectedTaskId = null;
    state.secondsRemaining = SESSION_SECONDS;
  }
  saveState();
  render();
  showStatus("Aufgabe gelöscht.");
}

function selectedOpenTask() {
  return state.tasks.find(
    (item) => item.id === state.selectedTaskId && !item.completed,
  ) ?? null;
}

function startOrPauseTimer() {
  if (timerHandle) {
    stopTimer();
    renderTimer();
    showStatus("Fokus-Session pausiert.");
    return;
  }

  const selected = selectedOpenTask();
  if (!selected) {
    showStatus("Wähle zuerst eine offene Aufgabe aus.");
    elements.title.focus();
    return;
  }

  timerHandle = window.setInterval(() => {
    state.secondsRemaining = Math.max(0, state.secondsRemaining - 1);
    saveState();
    renderTimer();

    if (state.secondsRemaining === 0) {
      finishSession();
    }
  }, 1000);

  renderTimer();
  showStatus("Fokus-Session gestartet.");
}

function stopTimer() {
  if (timerHandle) {
    window.clearInterval(timerHandle);
    timerHandle = null;
  }
}

function resetTimer() {
  stopTimer();
  state.secondsRemaining = SESSION_SECONDS;
  saveState();
  renderTimer();
  showStatus("Timer wurde zurückgesetzt.");
}

function finishSession() {
  stopTimer();
  state.completedSessions += 1;
  const selected = selectedOpenTask();
  if (selected) {
    selected.completed = true;
    selected.completedAt = new Date().toISOString();
  }
  state.selectedTaskId = null;
  state.secondsRemaining = SESSION_SECONDS;
  saveState();
  render();
  showStatus("Fokus-Session abgeschlossen. Gute Arbeit.");
}

function exportState() {
  const payload = {
    schemaVersion: 1,
    exportedAt: new Date().toISOString(),
    data: state,
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], {
    type: "application/json",
  });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `focusflow-export-${new Date().toISOString().slice(0, 10)}.json`;
  document.body.append(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
  showStatus("Datenexport wurde erstellt.");
}

function deleteAllData() {
  const accepted = window.confirm(
    "Alle Aufgaben, Sessions und Einstellungen in diesem Browser endgültig löschen?",
  );
  if (!accepted) return;
  stopTimer();
  localStorage.removeItem(STORAGE_KEY);
  state = initialState();
  render();
  showStatus("Alle lokalen FocusFlow-Daten wurden gelöscht.");
}

function render() {
  renderTasks();
  renderTimer();
  const completed = state.tasks.filter((task) => task.completed).length;
  const open = state.tasks.length - completed;
  elements.taskCount.textContent = `${open} offen`;
  elements.completedCount.textContent = String(completed);
  elements.sessionCount.textContent = String(state.completedSessions);
}

function renderTasks() {
  elements.list.replaceChildren();
  elements.empty.hidden = state.tasks.length > 0;

  for (const task of state.tasks) {
    const item = document.createElement("li");
    item.className = "task-item";
    item.dataset.selected = String(task.id === state.selectedTaskId && !task.completed);

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.className = "task-select";
    checkbox.checked = task.completed;
    checkbox.setAttribute("aria-label", `Aufgabe „${task.title}“ als erledigt markieren`);
    checkbox.addEventListener("change", () => toggleTask(task.id));

    const title = document.createElement("span");
    title.className = `task-title${task.completed ? " is-complete" : ""}`;
    title.textContent = task.title;

    const controls = document.createElement("div");
    controls.className = "task-controls";

    if (!task.completed) {
      const select = document.createElement("button");
      select.type = "button";
      select.className = "icon-button";
      select.textContent = task.id === state.selectedTaskId ? "Ausgewählt" : "Fokussieren";
      select.setAttribute("aria-pressed", String(task.id === state.selectedTaskId));
      select.addEventListener("click", () => selectTask(task.id));
      controls.append(select);
    }

    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "icon-button";
    remove.textContent = "Löschen";
    remove.setAttribute("aria-label", `Aufgabe „${task.title}“ löschen`);
    remove.addEventListener("click", () => deleteTask(task.id));
    controls.append(remove);

    item.append(checkbox, title, controls);
    elements.list.append(item);
  }

  const selected = selectedOpenTask();
  elements.selectedTask.textContent = selected?.title ?? "Keine Aufgabe ausgewählt";
}

function renderTimer() {
  const minutes = Math.floor(state.secondsRemaining / 60);
  const seconds = state.secondsRemaining % 60;
  elements.timer.textContent = `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
  elements.startPause.textContent = timerHandle ? "Pausieren" : "Starten";
  elements.startPause.setAttribute("aria-pressed", String(Boolean(timerHandle)));
  elements.timerState.textContent = timerHandle
    ? "Läuft"
    : state.secondsRemaining < SESSION_SECONDS
      ? "Pausiert"
      : "Bereit";
  elements.resetTimer.disabled = state.secondsRemaining === SESSION_SECONDS && !timerHandle;
}

function showStatus(message) {
  window.clearTimeout(statusTimeout);
  elements.appStatus.textContent = message;
  elements.appStatus.hidden = false;
  statusTimeout = window.setTimeout(() => {
    elements.appStatus.hidden = true;
  }, 4500);
}

elements.form.addEventListener("submit", (event) => {
  event.preventDefault();
  elements.error.hidden = true;
  const title = sanitizeTitle(elements.title.value);

  if (title.length < 3) {
    elements.error.textContent = "Die Aufgabe benötigt mindestens drei Zeichen.";
    elements.error.hidden = false;
    elements.title.focus();
    return;
  }

  if (state.tasks.some((task) => task.title.toLowerCase() === title.toLowerCase() && !task.completed)) {
    elements.error.textContent = "Diese offene Aufgabe existiert bereits.";
    elements.error.hidden = false;
    elements.title.focus();
    return;
  }

  addTask(title);
  elements.form.reset();
  elements.title.focus();
});

elements.startPause.addEventListener("click", startOrPauseTimer);
elements.resetTimer.addEventListener("click", resetTimer);
elements.exportData.addEventListener("click", exportState);
elements.deleteData.addEventListener("click", deleteAllData);

document.addEventListener("visibilitychange", () => {
  if (document.hidden && timerHandle) {
    saveState();
  }
});

window.addEventListener("beforeunload", saveState);

if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("./sw.js").catch((error) => {
      console.warn("Service Worker konnte nicht registriert werden.", error);
    });
  });
}

render();

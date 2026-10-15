-- FocusFlow educational example
-- Review against the current project, PostgreSQL version and Supabase documentation.
-- Apply through versioned migrations, never by blind copy into production.

create extension if not exists pgcrypto;

create type public.task_status as enum ('open', 'completed', 'archived');
create type public.session_status as enum ('active', 'completed', 'cancelled');

create table public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text check (display_name is null or char_length(display_name) between 1 and 80),
  timezone text not null default 'Europe/Berlin',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table public.projects (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  title text not null check (char_length(title) between 1 and 120),
  archived_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table public.tasks (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  project_id uuid references public.projects(id) on delete set null,
  title text not null check (char_length(title) between 1 and 240),
  status public.task_status not null default 'open',
  estimated_minutes integer check (estimated_minutes is null or estimated_minutes between 1 and 1440),
  completed_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table public.focus_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  task_id uuid references public.tasks(id) on delete set null,
  status public.session_status not null default 'active',
  planned_seconds integer not null check (planned_seconds between 60 and 14400),
  started_at timestamptz not null default now(),
  ended_at timestamptz,
  actual_seconds integer check (actual_seconds is null or actual_seconds between 0 and 86400),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint focus_sessions_end_after_start
    check (ended_at is null or ended_at >= started_at),
  constraint focus_sessions_completed_fields
    check (
      (status = 'active' and ended_at is null and actual_seconds is null)
      or
      (status in ('completed', 'cancelled') and ended_at is not null and actual_seconds is not null)
    )
);

create table public.ai_usage (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  request_type text not null check (request_type in ('task_breakdown')),
  model_key text not null,
  prompt_version text not null,
  input_hash text,
  input_tokens integer check (input_tokens is null or input_tokens >= 0),
  output_tokens integer check (output_tokens is null or output_tokens >= 0),
  cost_minor integer check (cost_minor is null or cost_minor >= 0),
  succeeded boolean not null default false,
  created_at timestamptz not null default now()
);

create index projects_user_id_idx on public.projects(user_id);
create index tasks_user_id_idx on public.tasks(user_id);
create index tasks_project_id_idx on public.tasks(project_id);
create index focus_sessions_user_id_idx on public.focus_sessions(user_id);
create index focus_sessions_task_id_idx on public.focus_sessions(task_id);
create index focus_sessions_user_status_idx on public.focus_sessions(user_id, status);
create index ai_usage_user_created_idx on public.ai_usage(user_id, created_at desc);

alter table public.profiles enable row level security;
alter table public.projects enable row level security;
alter table public.tasks enable row level security;
alter table public.focus_sessions enable row level security;
alter table public.ai_usage enable row level security;

-- Profiles
create policy "profiles_select_own"
on public.profiles for select to authenticated
using ((select auth.uid()) = id);

create policy "profiles_insert_own"
on public.profiles for insert to authenticated
with check ((select auth.uid()) = id);

create policy "profiles_update_own"
on public.profiles for update to authenticated
using ((select auth.uid()) = id)
with check ((select auth.uid()) = id);

-- Projects
create policy "projects_select_own"
on public.projects for select to authenticated
using ((select auth.uid()) = user_id);

create policy "projects_insert_own"
on public.projects for insert to authenticated
with check ((select auth.uid()) = user_id);

create policy "projects_update_own"
on public.projects for update to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

create policy "projects_delete_own"
on public.projects for delete to authenticated
using ((select auth.uid()) = user_id);

-- Tasks
create policy "tasks_select_own"
on public.tasks for select to authenticated
using ((select auth.uid()) = user_id);

create policy "tasks_insert_own"
on public.tasks for insert to authenticated
with check (
  (select auth.uid()) = user_id
  and (
    project_id is null
    or exists (
      select 1
      from public.projects p
      where p.id = project_id
        and p.user_id = (select auth.uid())
    )
  )
);

create policy "tasks_update_own"
on public.tasks for update to authenticated
using ((select auth.uid()) = user_id)
with check (
  (select auth.uid()) = user_id
  and (
    project_id is null
    or exists (
      select 1
      from public.projects p
      where p.id = project_id
        and p.user_id = (select auth.uid())
    )
  )
);

create policy "tasks_delete_own"
on public.tasks for delete to authenticated
using ((select auth.uid()) = user_id);

-- Focus sessions
create policy "focus_sessions_select_own"
on public.focus_sessions for select to authenticated
using ((select auth.uid()) = user_id);

create policy "focus_sessions_insert_own"
on public.focus_sessions for insert to authenticated
with check (
  (select auth.uid()) = user_id
  and (
    task_id is null
    or exists (
      select 1
      from public.tasks t
      where t.id = task_id
        and t.user_id = (select auth.uid())
    )
  )
);

create policy "focus_sessions_update_own"
on public.focus_sessions for update to authenticated
using ((select auth.uid()) = user_id)
with check (
  (select auth.uid()) = user_id
  and (
    task_id is null
    or exists (
      select 1
      from public.tasks t
      where t.id = task_id
        and t.user_id = (select auth.uid())
    )
  )
);

create policy "focus_sessions_delete_own"
on public.focus_sessions for delete to authenticated
using ((select auth.uid()) = user_id);

-- AI usage is intentionally readable by the user but writable only by a trusted server.
create policy "ai_usage_select_own"
on public.ai_usage for select to authenticated
using ((select auth.uid()) = user_id);

-- No INSERT/UPDATE/DELETE policy for normal authenticated clients.
-- A protected server component may use a privileged connection after independently
-- verifying identity, authorization, limits and input.

-- Additional production work:
-- 1. Restrict table/function grants explicitly.
-- 2. Add a controlled profile creation flow.
-- 3. Add updated_at triggers.
-- 4. Make session completion idempotent through a reviewed RPC or backend transaction.
-- 5. Test every policy with user A, user B and unauthenticated clients.
-- 6. Verify query plans and indexes with realistic data volumes.
-- 7. Add export/deletion jobs and backup-restore deletion journal.

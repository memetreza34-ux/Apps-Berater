-- FocusFlow reference migration
-- Review and adapt before production use.

create extension if not exists pgcrypto;

create table public.projects (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  title text not null check (char_length(btrim(title)) between 1 and 120),
  archived_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table public.tasks (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  project_id uuid references public.projects(id) on delete cascade,
  title text not null check (char_length(btrim(title)) between 1 and 240),
  status text not null default 'open' check (status in ('open', 'completed', 'cancelled')),
  estimated_minutes integer check (estimated_minutes is null or estimated_minutes between 1 and 1440),
  completed_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint tasks_completed_at_matches_status check (
    (status = 'completed' and completed_at is not null)
    or (status <> 'completed' and completed_at is null)
  )
);

create table public.focus_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  task_id uuid references public.tasks(id) on delete set null,
  status text not null default 'running' check (status in ('running', 'completed', 'cancelled')),
  started_at timestamptz not null default now(),
  ended_at timestamptz,
  duration_seconds integer check (duration_seconds is null or duration_seconds between 0 and 86400),
  created_at timestamptz not null default now(),
  constraint focus_sessions_end_state check (
    (status = 'running' and ended_at is null)
    or (status <> 'running' and ended_at is not null)
  )
);

create index projects_user_id_created_at_idx
  on public.projects (user_id, created_at desc);
create index tasks_user_id_status_created_at_idx
  on public.tasks (user_id, status, created_at desc);
create index tasks_project_id_idx
  on public.tasks (project_id);
create index focus_sessions_user_id_started_at_idx
  on public.focus_sessions (user_id, started_at desc);
create index focus_sessions_task_id_idx
  on public.focus_sessions (task_id);

alter table public.projects enable row level security;
alter table public.tasks enable row level security;
alter table public.focus_sessions enable row level security;

revoke all on public.projects from anon;
revoke all on public.tasks from anon;
revoke all on public.focus_sessions from anon;

grant select, insert, update, delete on public.projects to authenticated;
grant select, insert, update, delete on public.tasks to authenticated;
grant select, insert, update, delete on public.focus_sessions to authenticated;

create policy projects_select_own
on public.projects
for select
to authenticated
using ((select auth.uid()) = user_id);

create policy projects_insert_own
on public.projects
for insert
to authenticated
with check ((select auth.uid()) = user_id);

create policy projects_update_own
on public.projects
for update
to authenticated
using ((select auth.uid()) = user_id)
with check ((select auth.uid()) = user_id);

create policy projects_delete_own
on public.projects
for delete
to authenticated
using ((select auth.uid()) = user_id);

create policy tasks_select_own
on public.tasks
for select
to authenticated
using ((select auth.uid()) = user_id);

create policy tasks_insert_own
on public.tasks
for insert
to authenticated
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

create policy tasks_update_own
on public.tasks
for update
to authenticated
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

create policy tasks_delete_own
on public.tasks
for delete
to authenticated
using ((select auth.uid()) = user_id);

create policy focus_sessions_select_own
on public.focus_sessions
for select
to authenticated
using ((select auth.uid()) = user_id);

create policy focus_sessions_insert_own
on public.focus_sessions
for insert
to authenticated
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

create policy focus_sessions_update_own
on public.focus_sessions
for update
to authenticated
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

create policy focus_sessions_delete_own
on public.focus_sessions
for delete
to authenticated
using ((select auth.uid()) = user_id);

comment on table public.projects is 'FocusFlow projects; rows are private to auth.uid().';
comment on table public.tasks is 'FocusFlow tasks; project ownership is validated by RLS.';
comment on table public.focus_sessions is 'FocusFlow focus sessions; task ownership is validated by RLS.';

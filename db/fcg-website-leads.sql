-- FCG website forms: schema `fcg_website` on Supabase project accomy-projects (iedubjxycyvqptkcezlp).
-- Applied via the Management API on 2026-10-26; fcg_website added to the exposed schemas. Server key: per-app sb_secret `fcg_website`.
-- Same shape as accomy.com's `website` schema, kept separate so FCG and Accomy leads never mix.
-- Source of truth for /api/book-demo and /api/subscribe; the Lark Base tables are a mirror. Re-runnable.

create schema if not exists fcg_website;

create table if not exists fcg_website.leads (
  id          uuid primary key default gen_random_uuid(),
  form        text not null check (form in ('book_demo')),
  page_uri    text,
  name        text not null,
  email       text not null,
  company     text not null,
  job_title   text,
  message     text,
  details     jsonb not null default '{}'::jsonb,
  created_at  timestamptz not null default now()
);
create index if not exists leads_created_at_idx on fcg_website.leads (created_at desc);
create index if not exists leads_email_idx on fcg_website.leads (lower(email));

-- Single opt-in: consent_at is the submission moment.
-- ponytail: add a confirmation token + confirm route (double opt-in) before this list is ever mailed.
create table if not exists fcg_website.subscribers (
  id          uuid primary key default gen_random_uuid(),
  email       text not null,
  source      text not null check (source in ('blog_newsletter')),
  page_uri    text,
  consent_at  timestamptz not null default now(),
  created_at  timestamptz not null default now()
);
create unique index if not exists subscribers_email_key on fcg_website.subscribers (lower(email));

-- The server uses the sb_secret key (service_role); no browser ever reads these tables, so RLS stays off
-- and anon/authenticated get no table grants. Also add fcg_website to Settings > API > Exposed schemas.
grant usage on schema fcg_website to service_role;
grant all on all tables in schema fcg_website to service_role;
alter default privileges in schema fcg_website grant all on tables to service_role;

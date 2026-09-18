-- Snapshot of legal-ops-intake/supabase/migrations/*.sql (CREATE TABLE / ALTER TABLE
-- statements only — no data, no functions, no RLS policies).
-- Source: sibling repo legal-ops-intake, path supabase/migrations/
-- This is a versioned copy, not a live read of the source repo — it may be stale relative
-- to the current state of legal-ops-intake. Re-copy it if those migrations change.

-- From 20260907120000_create_schema.sql
create table lawyers (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  email text not null unique,
  auth_user_id uuid unique references auth.users(id) on delete set null,
  active boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table requests (
  id uuid primary key default gen_random_uuid(),

  request_type text not null check (request_type in (
    'pontual_query',
    'nda',
    'renewal_no_changes',
    'new_contract_corvina_paper',
    'third_party_draft_review'
  )),

  requesting_department text not null,

  -- A company, never an individual.
  counterparty_name text,

  estimated_value_band text check (estimated_value_band in (
    'under_10k',
    '10k_50k',
    '50k_250k',
    '250k_1m',
    'over_1m'
  )),

  desired_date date not null,

  justification text,

  description text,

  assigned_lawyer_id uuid references lawyers(id) on delete set null,

  status text not null default 'new' check (status in (
    'new',
    'in_progress',
    'on_hold',
    'completed',
    'cancelled'
  )),

  -- Data-processing questions: booleans describing the operation the request
  -- concerns, never the personal data itself.
  involves_customer_data boolean not null default false,
  involves_employee_data boolean not null default false,
  involves_third_party_data boolean not null default false,
  involves_international_transfer boolean not null default false,

  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table status_transitions (
  id uuid primary key default gen_random_uuid(),
  request_id uuid not null references requests(id) on delete cascade,
  previous_status text,
  new_status text not null,
  changed_at timestamptz not null default now()
);

-- From 20260909140000_add_triage_lane.sql
alter table requests
  add column triage_lane text not null check (triage_lane in (
    'express',
    'standard',
    'priority'
  ));

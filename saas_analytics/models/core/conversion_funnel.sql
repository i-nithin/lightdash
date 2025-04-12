{{ config(materialized='view') }}

with visitors as (
    select
        date_trunc('month', visit_date) as month,
        count(distinct user_id) as visitors
    from {{ ref('stg_visits') }}
    group by 1
),

signups as (
    select
        date_trunc('month', signup_date) as month,
        count(distinct id) as signups
    from {{ ref('stg_users') }}
    group by 1
),

paying_users as (
    select
        date_trunc('month', payment_date) as month,
        count(distinct user_id) as paying_users
    from {{ ref('stg_payments') }}
    group by 1
)

select
    coalesce(v.month, s.month, p.month) as month,
    v.visitors,
    s.signups,
    p.paying_users
from visitors v
full outer join signups s on v.month = s.month
full outer join paying_users p on coalesce(v.month, s.month) = p.month
order by month

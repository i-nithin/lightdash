{{ config(materialized='view') }}

with cohorts as (
    select
        id as user_id,
        date_trunc('month', signup_date) as cohort_month
    from {{ ref('stg_users') }}
),

visits as (
    select
        user_id,
        date_trunc('month', visit_date) as visit_month
    from {{ ref('stg_visits') }}
    group by 1, 2
),

joined as (
    select
        c.cohort_month,
        v.visit_month,
        count(distinct v.user_id) as retained_users
    from cohorts c
    join visits v on c.user_id = v.user_id
    group by 1, 2
)

select
    cohort_month,
    visit_month,
    retained_users
from joined
order by cohort_month, visit_month

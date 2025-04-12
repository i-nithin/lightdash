{{ config(materialized='view') }}

select
    date_trunc('month', signup_date) as month,
    source,
    count(*) as signups
from {{ ref('stg_users') }}
group by 1, 2
order by month

{{ config(materialized='view') }}

select
    date_trunc('month', end_date) as month,
    count(*) as churned_subscriptions
from {{ ref('stg_subscriptions') }}
where end_date is not null
group by 1
order by month

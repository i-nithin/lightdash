{{ config(materialized='view') }}

with active_subscriptions as (
    select
        date_trunc('month', start_date) as month,
        sum(price_usd) as mrr
    from {{ ref('stg_subscriptions') }}
    where end_date is null
    group by 1
)

select * from active_subscriptions
order by month

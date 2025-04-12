with source as (
    select * from {{ source('public', 'subscriptions') }}
)

SELECT
  id,
  user_id,
  start_date,
  end_date,
  price_usd
FROM source

with source as (
    select * from {{ source('public', 'payments') }}
)

SELECT
  id,
  user_id,
  amount,
  payment_date
FROM source

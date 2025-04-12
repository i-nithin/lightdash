with source as (
    select * from {{ source('public', 'visits') }}
)

SELECT
  id,
  user_id,
  visit_date,
  page
FROM source

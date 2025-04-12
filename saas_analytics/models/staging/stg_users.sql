with source as (
    select * from {{ source('public', 'users') }}
)

select
    id,
    name,
    email,
    signup_date,
    source
from source

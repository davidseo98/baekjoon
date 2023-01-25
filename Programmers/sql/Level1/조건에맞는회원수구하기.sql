-- 코드를 입력하세요
SELECT count(user_id)
from user_info
where year(joined) = 2021 and 20 <= age and age <= 29
-- 20 <= age <= 29라고 하면 틀린다
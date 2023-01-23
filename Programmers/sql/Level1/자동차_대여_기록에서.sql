-- 코드를 입력하세요

SELECT HISTORY_ID, 
       CAR_ID, 
       DATE_FORMAT(START_DATE,'%Y-%m-%d') AS START_DATE, 
       DATE_FORMAT(END_DATE,'%Y-%m-%d') AS END_DATE, 
       CASE WHEN datediff(end_date, start_date) + 1 >= 30 THEN '장기 대여'
            ELSE '단기 대여' 
       END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE month(start_date) = 09 and year(start_date) = 2022 
ORDER BY HISTORY_ID DESC
-- 코드를 입력하세요
SELECT CAR_ID, round(avg(datediff(end_date, start_date)+1),1) AVERAGE_DURATION from car_rental_company_rental_history group by car_id having AVERAGE_DURATION >=7 order by AVERAGE_DURATION desc, car_id desc;

select c.car_id, c.car_type, round(30*c.daily_fee*(100 - p.discount_rate) * 0.01,0) as FEE from car_rental_company_car c left join (
        select car_id, end_date from car_rental_company_rental_history ) h on c.car_id = h.car_id left join (
    select car_type, discount_rate from car_rental_company_discount_plan where duration_type like ('%30%')) p on c.car_type = p.car_type  where c.car_type in ('SUV','세단') and round(30*c.daily_fee*(100 - p.discount_rate) * 0.01,0) >= 500000 and round(30*c.daily_fee*(100 - p.discount_rate) * 0.01,0) < 2000000 group by car_id having max(h.end_date) < '2022-11-01' order by FEE desc, c.car_type, c.car_id desc;

# select * from car_rental_company_rental_history group by car_id having max(end_date) < '2022-11-01'


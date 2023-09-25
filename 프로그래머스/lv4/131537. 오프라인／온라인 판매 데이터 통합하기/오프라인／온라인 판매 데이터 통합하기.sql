select date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, null as user_id, sales_amount
from offline_sale
where sales_date between date('2022-03-01') and date('2022-03-31')
union all
select date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, ifnull(user_id,null), sales_amount
from online_sale
where sales_date between date('2022-03-01') and date('2022-03-31')
order by sales_date, product_id, user_id;
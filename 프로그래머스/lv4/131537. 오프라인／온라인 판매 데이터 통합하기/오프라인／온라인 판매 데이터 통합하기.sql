select date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, ifnull(user_id,null), sales_amount
from offline_sale;
order by sales_date, product_id, user_id;
select product_code, p.price * sum(o.sales_amount) as SALES from product as p, offline_sale as o
where p.product_id = o.product_id
group by product_code
order by sales desc, product_code
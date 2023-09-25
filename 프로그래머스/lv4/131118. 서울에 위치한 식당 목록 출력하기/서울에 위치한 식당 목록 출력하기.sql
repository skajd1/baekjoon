select i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, round(avg(r.review_score),2) as score
from rest_info as i, rest_review as r
where i.address like '서울%' and i.rest_id = r.rest_id
group by i.rest_id
order by score desc, i.favorites desc;

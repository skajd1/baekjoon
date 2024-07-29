select i.item_id, i.item_name, i.rarity 
from ITEM_INFO as i
LEFT JOIN ITEM_TREE as t
on i.item_id = t.parent_item_id
where t.parent_item_id is null
order by i.item_id desc;
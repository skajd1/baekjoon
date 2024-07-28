-- 코드를 입력하세요
SELECT i.flavor from first_half as h, icecream_info as i where h.flavor = i.flavor and h.total_order > 3000 and i.ingredient_type = 'fruit_based' order by h.total_order desc;

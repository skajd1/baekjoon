-- 코드를 입력하세요
SELECT h.flavor from first_half h left join (
    select flavor, sum(total_order) s from july group by flavor) j on h.flavor = j.flavor order by (h.total_order + j.s) desc limit 3
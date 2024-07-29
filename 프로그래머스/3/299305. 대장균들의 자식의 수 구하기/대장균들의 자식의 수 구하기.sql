select a.ID, (
    select count(*) from ECOLI_DATA as b where b.parent_id = a.ID) as CHILD_COUNT from ECOLI_DATA as a order by a.ID
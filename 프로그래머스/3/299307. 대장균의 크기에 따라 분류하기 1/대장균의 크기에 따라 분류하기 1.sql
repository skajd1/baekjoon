-- 코드를 작성해주세요
select ID, IF(SIZE_OF_COLONY <= 100, 'LOW', IF(SIZE_OF_COLONY <= 1000, 'MEDIUM', 'HIGH')) as SIZE from ECOLI_DATA order by ID;
-- 코드를 작성해주세요
select round((sum(length) + (select count(*) from fish_info where length is null) * 10)/count(*),2) as AVERAGE_LENGTH from fish_info
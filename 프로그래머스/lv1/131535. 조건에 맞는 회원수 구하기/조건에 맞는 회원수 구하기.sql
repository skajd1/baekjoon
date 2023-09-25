select count(*) from user_info
where joined between date('2021-01-01') and date('2021-12-31')
and age between 20 and 29
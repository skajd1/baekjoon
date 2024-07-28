-- 코드를 입력하세요
SELECT MEMBER_ID,MEMBER_NAME,GENDER,date_format(DATE_OF_BIRTH,'%Y-%m-%d') from member_profile where MONTH(DATE_OF_BIRTH) = 3 and TLNO is NOT NULL and GENDER = 'W' order by MEMBER_ID;
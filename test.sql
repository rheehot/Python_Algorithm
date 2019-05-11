select BRANCH_ID, sum(SALARY) as TOTAL from EMPLOYEES group by BRANCH_ID;
--SELECT
--테이블별칭.조회할칼럼,
--테이블별칭.조회할칼럼
--FROM 기준테이블 별칭
--FULL OUTER JOIN 조인테이블 별칭 ON 기준테이블별칭.기준키 = 조인테이블별칭.기준키 .....
SELECT BRANCH_ID, SUM(SELLINGS.PRICE) as TOTAL from EMPLOYEES JOIN SELLINGS.EMPLOYEE_ID ON EMPLOYEES.ID;

select *
from EMPLOYEES left join SELLINGS
union
select *
from EMPLOYEES right join SELLINGS;

select BRANCH_ID, sum(SELLINGS.PRICE) as TOTAL from EMPLOYEES join SELLINGS group by BRANCH_ID;
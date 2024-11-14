-- join
-- inner join(equi join,non-equi join),self join,outer join

select employee_id,emp_name,a.department_id from employees a , departments b where a.department_id = b.department_id;

select * from stu_grade;

-- 두 테이블의 공통적인 컬럼 없이 
-- avg 값을 가지고 다른 컬럼을 다른 테이블에서 가져와 출력
select * from students,stu_grade where avg between loavg and hiavg;

-- self join : 자기 자신을 2번 호출하여 원하는 데이터를 출력
select a.employee_id, a.emp_name, a.manager_id,b.emp_name from employees a, employees b where a.manager_id = b.manager_id;

select * from stu;

update stu a set result = (
select results from (
select no, avg, grade as results from stu, stu_grade where avg between loavg and hiavg) b
where a.no = b.no
);

-- rank() over()
select * from stu;

update stu set rank = 0;

select no, name, avg, rank, rank() over(order by avg desc) as ranks from stu;

update stu a set rank = (
select ranks from(
select no, dense_rank() over(order by avg desc) as ranks from stu) b
where a.no = b.no
);

commit;

select employee_id,emp_name,manager_id from employees;  -- 107

select count(manager_id) from employees where manager_id is not null;

select count(nvl(manager_id,0)) from employees;
select count(nvl(to_char(manager_id),'ceo')) from employees;

-- outer join : 2개 중의 하나의 컬럼에서 모든 데이터(null값 포함)을 출력하기 위한 조인방법
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a,employees b
where a.manager_id = b.employee_id(+);

-- equi_join
select employee_id, emp_name, b.department_id, department_name from employees a,departments b
where a.department_id=b.department_id(+);

select department_id from employees;

-- ansi cross join
select * from employees cross join departments;
-- cross join
select * from employees,departments;

-- ansi inner join
select a.department_id, department_name
from employees a inner join departments b
on a.department_id = b.department_id;

-- ansi join : using 공통적으로 사용
select department_id,department_name
from employees inner join departments
using (department_id);

-- equi_join
select a.department_id, department_name
from employees a,departments b
where a.department_id = b.department_id;

-- ansi join : natural join 두 개의 공통부분의 컬럼이 있으면 자동으로 인식해서 검색
select department_id, department_name from employees natural join departments;

select * from employees a natural join departments b;


-- outer join (left,right,full) null값이 붙은 방향을 적으면 됨 / 둘다 하려면 full 넣으면됨
select a.department_id,department_name from employees a left outer join departments b
on a.department_id = b.department_id;

-- 오라클 inner join -> 두 개의 컬럼에 (+)붙으면  error : outer join
select employee_id,emp_name,a.department_id,department_name
from employees a, departments b 
where a.department_id = b.department_id(+);
----------------------------------------------------------------------------------union
select * from students;
select * from employees;

select * from students where total >= 250;   -- 25  
select * from students where name like '%a%';   -- 35

select * from students where total >= 250
union all
select * from students where name like '%a%'; -- 60

select * from students where total >= 250 or name like '%a%';

select employee_id, emp_name from employees;
select no,name from students;

-- union : 같은 테이블,다른 테이블 모두 사용 가능하고 컬럽의 타입만 맞으면 모두 출력
select employee_id, emp_name from employees
union
select no,name from students;

-- 자유게시판, 공지사항, 이벤트, 종합게시판 등 통합적으로 검색해서 출력하고 싶을 때 사용
select employee_id,emp_name,no,name from employees, students;

select * from students;
select * from employees;

-- department_id가 50인 사원 출력
select emp_name,d.department_id,department_name from employees e,departments d where d.department_id = 50 and e.department_id=d.department_id;
-- salary 5000 and 8000 사원 출력
select emp_name,d.department_id,department_name from employees e,departments d where salary >= 5000 and salary <= 8000 and e.department_id=d.department_id;

select emp_name,d.department_id,department_name from employees e,departments d where d.department_id = 50 and e.department_id=d.department_id
union
select emp_name,d.department_id,department_name from employees e,departments d where salary >= 5000 and salary <= 8000 and e.department_id=d.department_id;


-- departments 부서 검색(중복없이 출력)
select department_id,department_name from departments a where exists
( select 1 from employees b where a.department_id =  b.department_id);

-- employees에 없는 부서 검색(중복없이 출력)
select distinct department_id from departments;

select name,mdate from member
union
select name,sdate from students;

select * from board;

drop table board2;

create table board2 (
	bno number(4),
	btitle VARCHAR2(1000),
	bcontent clob,
	id VARCHAR2(30),
	bgroup number(4),
	bstep number(4),
	bindent number(4),
	bhit number(4),
	bdate DATE,
	bfile VARCHAR2(100)
);

select * from board2;

commit;

delete board2 where bno = 98;

select * from board2 where bno between 1 and 10;

-- 중간중간 빠진 번호를 채워 순번을 다시 부여
select rownum,bno,btitle,bdate from board2;

-- rownum 서브쿼리 사용
select rnum,bno,btitle from
(select rownum rnum,bno,btitle from(
select bno,btitle from board2 order by bdate desc))
where rnum between 20 and 30;

-- row_number() order : 정렬한 후 번호를 부여
select row_number() over(order by bdate desc) rnum,bno,btitle,bdate from board2;

select rnum,bno,btitle from(
select row_number() over(order by bdate desc) rnum,bno,btitle,bdate from board2)
where rnum between 11 and 20;

-- row_number()로 정렬해서 모든 컬럼 가져오기
select row_number() over(order by bdate desc) rnum, a.* from board2 a;

select * from(
select row_number() over(order by bdate desc) rnum, a.* from board2 a)
where rnum between 11 and 20;

select rnum,bno,btitle from
(select rownum rnum,bno,btitle from(
select bno,btitle from board2 order by bdate desc))
where rnum between 20 and 30;

select * from
(select rownum rnum,a.* from(select * from board2 order by bdate desc) a)
where rnum between 11 and 20;

select rownum, a.* from (
select rownum,no,name,avg,rank() over(order by avg desc) from students
) a;

select rownum,no,name,avg,rank() over(order by avg desc) from students;


select * from(
select rownum rnum, a.* from (
select rownum,no,name,avg,rank() over(order by avg desc) from students
) a) where rnum between 11 and 20;

select * from (
select row_number() over(order by avg desc) rnum,a.* from students a)
where rnum between 11 and 20;

select * from students;

select no,rank() over(order by avg desc) ranks from students;

update students a set rank = (
select ranks from (select no,rank() over(order by avg desc) ranks from students) b
where a.no = b.no
);

commit;
----------------------------------------------------------------------------------view
-- 상담원 : 사원들 전화로 사원들에게 마케팅하려고 함 / 100명에게 사원 테이블 오픈 데공해달라고 요청 : 마케팅

select * from employees;

create or replace view employees_view as select employee_id,emp_name,email,phone_number,hire_date from employees;


select * from employees_view;

-- 뷰 생성
create or replace view emp_view
as select e.employee_id,emp_name,email,phone_number,hire_date,d.department_id,department_name from employees e,departments d
where e.department_id = d.department_id;

select * from emp_view;

drop view emp_view;

select * from employees_view;
-- view 컬럼 코멘트(주석 - 설명문) 추가
comment on column employees_view.employee_id is '사원번호';
-- 컬럼 코멘트 주석확인
select * from user_col_comments;
-- 테이블 코멘트 주석확인
select * from user_tab_comments;

select employee_id as e_id, emp_name as e_name from employees;

-- 컬럼 별칭 선언 : 상단에 미리 정의하면 쿼리문 컬럼 순서대로 별칭이 부여됨
create or replace view emp_view
as
select employee_id as e_id, emp_name as e_name from employees;

select * from emp02;

drop table emp02;

create table emp02(
 employee_id number(6),
 emp_name varchar2(80),
 hire_date date,
 salary number(8,2),
 department_id number(6)
);

insert into emp02(employee_id,emp_name,hire_date,salary,department_id)
select employee_id,emp_name,hire_date,salary,department_id from employees;

select * from emp02_view;


create or replace view emp02_view
as
select employee_id,emp_name,hire_date
from emp02;

select * from emp02_view order by employee_id;

-- 단순 view : 한 개의 테이블로 구성된 것
-- update, delete, insert 가능

-- 복합 view : 2개 이상 테이블 조인 함수사용, group by 같은 경우는 update, delete, insert 불가
-- update, delete, insert 가능
update emp02_view set emp_name='홍길동' where employee_id = 101;

select * from emp02;

select max(no) from students;




commit;

insert into emp02_view values(
207,'유관순',sysdate
);

select * from emp02_view order by employee_id desc;

select * from emp02;
select * from emp02_view;

alter table emp02 modify salary number(8,2) not null;

rollback;

commit;
delete emp02 where employeed_id = 207;







select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students;

select * from students where name like '%a%';


select * from students order by rank;

update students a set rank = (
select ranks from (select no,rank() over(order by avg desc) ranks from students) b
where a.no = b.no
);

commit;

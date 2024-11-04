create table emp02(
 empno number(4) unique,
 ename varchar2(30) not null,
 job varchar2(30),
 deptno number(2)
);


insert into emp02 values(
 1, '홍길동', 'clerk', 2
);
-- null 무결성제약조건에 들어가면 좋지않음
insert into emp02 values(
 2, '유관순',null,null
);
insert into emp02 values(
 null, '이순신', null, 2
);
insert into emp02 values(
 null, '강감찬', null, 2
);
-- unique 중복된 값 넣을 수 없음
insert into emp02 values(
 3, '김구', null, 2
);

select * from emp02;

delete emp02 where empno is null;
-- 제약조건 변경 alter
alter table emp02 modify empno number(4) not null;
alter table emp02 modify empno;

commit;

drop table emp02;

-- pk_emp02_empno 별칭
alter table emp02 add constraint pk_emp02_empno primary key(empno);

create table emp02(
 empno number(4) primary key,
 ename varchar2(30) not null,
 job varchar2(30),
 deptno number(2)
);

drop table mem;

create table mem(
 id varchar2(30) primary key,
 pw varchar2(30) not null,
 name varchar2(100) default '무명',
 gender varchar2(6) check(gender in ('Male','Female'))     -- male, female, MALE, FEMALE 입력시 에러
);

insert into mem values(
 'aaa','1111','홍길동','Male'
);
insert into mem values(
 'bbb','1111','유관순','Female'
);

commit;

select * from board;

create table board2(
 bno number(4) primary key,
 btitle varchar2(1000) not null,
 id varchar2(30),
 -- 외래키로 등록이되면 부모키(mem)에 해당 값이 없을시 자식키(board2) 에러
 constraint fk_board2_id foreign key(id) references mem(id)
);

select * from mem;
 -- 자식레코드(board2)를 삭제해야 부모레코드(mem) 삭제가능
delete mem where id='aaa';

insert into board2 values(
 1,'제목1','aaa'
);
insert into board2 values(
 4,'제목4','bbb'
);

commit;

select * from board2;

alter table board2 drop constraint fk_board2_id;

-- on delete cascade : 부모키(mem)가 삭제되면 외래키로 등록된 자식키(board2) 값 삭제
alter table board2 add constraint fk_board2_id foreign key (id) references mem(id) on delete cascade;

-- 부모테이블 'aaa' 값 삭제시, 자식테이블의 'aaa' 값 삭제
delete mem where id='aaa';

-- on delete sell null : 부모키 삭제시, 외래키로 등록된 값을 null로 변경
-----------------------------------------------------------------------------------논리의사용
drop table mem;
drop table board2;

create table mem(
 id varchar2(30) primary key,
 pw varchar2(100) not null,
 name varchar2(100),
 deptno number(4)
);


insert into mem values(
 'aaa','1111','홍길동',10
);
insert into mem values(
 'ccc','1111','이순신',30
);

commit;

select * from mem;

-- 10 '총무부' / 20 '인사부' / 30 '마케팅'
select id,pw,name,deptno from mem;
select id,pw,name,deptno,decode(deptno,10,'총무부',20,'인사부',30,'마케팅') from mem;


select * from employees;

-- clerk 5% / rep 10% / man 15%

select * from employees;

--select substr(job_id,4) j_id from employees where lower(substr(job_id,4)) in('clerk','rep','man');
select substr(job_id,4) j_id, salary, decode(substr(job_id,4),'CLERK',salary*1.05,'REP',salary*1.1,'MAN',salary*1.15) sal from employees where substr(job_id,4) in('CLERK','REP','MAN');


create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);

commit;

select * from lavel_data;

--  1 : 100p 2 : 1000p 3 : 5000p 4 : 10000p 5 : 20000p
-- decode : 조건이 정확하게 일치(= 비교연산자)해야만 함
select id, lavel, decode(lavel,1,100,2,1000,3,5000,4,10000,5,20000)|| 'p' point from lavel_data;

select * from mem;
-- case : 다양한 비교연산자를 이용하여 조건을 제시할 수 있으므로 범위를 지정할 수잇음 = if문과 같음
select id,pw,name,deptno,
case
when deptno= 10 then '총무부'
when deptno= 20 then '인사부'
when deptno= 30 then '마케팅'
end as deptName
from mem;

select id, lavel, decode(lavel,1,5000,2,5000,3,5000,4,20000,5,20000)|| 'p' point from lavel_data;
select id, lavel, case
when lavel >= 1 and lavel <=3 then 5000
when lavel >= 4 and lavel <=5 then 20000
end|| 'p' as point
from lavel_data;

select * from students;

select no, name, kor, eng, math, total, avg, rank, sdate, case
when avg >= 90 then 'A'
when avg >= 80 and avg <90 then 'B'
when avg >= 70 and avg <80 then 'C'
when avg <70 then '-'
end as result
from students;


create table stu as select * from students;

select * from stu;

alter table stu add result varchar2(2);

select no, name, kor, eng, math, total, avg, rank, sdate, case
when avg >= 90 then 'A'
when avg >= 80 and avg <90 then 'B'
when avg >= 70 and avg <80 then 'C'
when avg <70 then '-'
end as result
from stu;

-- 파이썬보다 오라클에서 처리하면 더 빠름
update stu set result= (
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end
);


commit;
-- rank over() 순위구현 함수
select no,name,total, rank() over(order by total desc) from stu order by no;
-- dense_rank() : 공동순위의 경우 2,2 중복순위가 아닌 차등순위로 분배함 2,3
select no,name,total, dense_rank() over(order by total desc) from stu order by no;

-- 2중 쿼리문
select ranks from (select rank() over(order by total desc) ranks from stu);

update stu a set rank=(
select ranks from (select no,rank() over(order by total desc) as ranks from stu) b
where b.no = a.no
);

select * from stu;


select emp_name,salary,case
when salary<5000 then salary*1.15
when salary>=5000 and salary<=8000 then salary*1.1
when salary>8000 then salary*1.05
end as sal
from employees;

select * from employees;

select emp_name, salary, case
when emp_name like '%D%' then salary*1.1
when emp_name like '%M%' then salary*1.05
else salary
end sal
from employees;

select * from employees;

select department_id, commission_pct from employees where commission_pct is not null;

select count(*) from employees where commission_pct is not null;
select department_id, count(*) from employees group by department_id order by department_id;

select department_id,avg(salary) from employees group by department_id;

-- 단일함수 조건문 where / 그룹함수 조건문 having
select department_id,avg(salary),count(salary) from employees
having avg(salary)>=7000
group by department_id;

select department_id, avg(salary) from employees group by department_id;

select emp_name,department_id, salary from employees where salary < avg(salary);

-- 전체 평균월급
select avg(salary) from employees;
-- 부서별 평균월급
select department_id, count(*) from employees 
where salary<(select avg(salary) from employees)
group by department_id;

select salary from employees where department_id = 20;

-- 평균 월급이 5000이하인 부서별 인원수 출력
select department_id,avg(salary),count(salary) from employees
group by department_id
having avg(salary)<=5000;


-- 부서별 평균월급보다 적게 받는 사원 출력 
select department_id,emp_name,salary from employees a
where salary < (
select salarys from(
select department_id,avg(salary) salarys from employees
group by department_id) b
where a.department_id = b.department_id
)
group by department_id,emp_name,salary;


-- 부서별 평균월급보다 적게 받는 사원수 출력 
select department_id,count(*) from employees a
where salary < (
select salarys from(
select department_id,avg(salary) salarys from employees
group by department_id) b
where a.department_id = b.department_id
)
group by department_id
order by department_id
;

-- 부서별 최대급여&최소급여 (최대급여 >= 5000)
select nvl(department_id,0),max(salary),min(salary) from employees group by department_id having max(salary)>=5000;


-----------------------------------------------------------------------------------join

select * from departments;

select * from employees;

select emp_name,department_id from employees where emp_name = 'Donald OConnell';

select department_id,department_name from departments where department_id = '50';

-- 1. cross join : 특별한 키워드 없이 두개의 테이블 검색하는 것.
select * from employees;   -- 107
select * from departments;  -- 27

select count(*) from employees,departments; -- 107*27 = 2889
select * from employees,departments;
-- 2. inner join(equi join,non-equi join) : 같은 컬럼을 비교해서 두개의 테이블을 검색
select * from employees,departments
where employees.department_id = departments.department_id;

select * from member; -- 101
select * from board; -- 5
-- equi join
select bno, btitle,bcontent,a.id,email from member a,board b where a.id=b.id;

select * from jobs;
select * from employees;
select * from departments;

select employee_id,emp_name,j.job_id,job_title from jobs j,employees e where j.job_id = e.job_id;
select employee_id,emp_name,j.job_id,job_title from jobs j,employees e where j.job_id = e.job_id and j.job_id = 'SH_CLERK';

select employee_id,emp_name,d.department_id,department_name,j.job_id,job_title
from jobs j,employees e,departments d
where j.job_id = e.job_id and e.department_id = d.department_id;

select * from member;
select * from board;

select bno,btitle,bcontent,name,bgroup,bindent,bstep,bhit,bdate,bfile from member m,board b where m.id=b.id;

select * from employees;

-- 평균 월급보다 적은 사원 출력
select employee_id,emp_name,salary,e.department_id,department_name
from employees e,departments d
where e.department_id = d.department_id and salary < (select avg(salary) from employees);

-- 부서별 평균월급
select department_id,avg(salary) salarys from employees
group by department_id;


-- 부서별 평균 원급보다 적은 사원 출력
select employee_id,emp_name,salary,e.department_id,department_name
from employees e,departments d
where e.department_id = d.department_id
and  -- 부서별 평균월급보다 작은 사원 출력 ↓
salary < (
select salarys from(
select department_id,avg(salary) salarys from employees 
group by department_id) c
where e.department_id = c.department_id
);

select * from employees;
select * from departments;
select * from jobs;

select emp_name,employee_id,department_name,d.department_id,j.job_id,job_title
from employees e, jobs j, departments d
where e.department_id = d.department_id and e.job_id = j.job_id
and substr(j.job_id,4) in ('CLERK','MAN');


select * from customers;
select cust_city from customers order by cust_city;

select salary from employees order by salary;

create table salgrade(
 grade varchar2(10),
 losal number(6),
 hisal number(6)
);
drop table salgreade;

insert into salgrade values(
 'A등급',10001,12000
);
insert into salgrade values(
 'B등급',8001,10000
);
insert into salgrade values(
 'C등급',6001,8000
);
insert into salgrade values(
 'D등급',4001,6000
);
insert into salgrade values(
 'E등급',2000,4000
);

select * from salgrade;

commit;

-- salary 등급 넣으려고 함
select salary from employees;

-- non-equi join : 두 테이블 간 같은 컬럼이 없으면서, 두 테이블의 값을 비교해서 출력
select emp_name,salary,grade from employees,salgrade
where salary between losal and hisal;

alter table stu modify result varchar2(20);

create table stu_grade(
 grade varchar2(10),
 loavg number(5,2), -- 소수점 99.99 
 hiavg number(5,2)
);

drop table stu_grade;

insert into stu_grade values(
 'A등급',90,100
);
insert into stu_grade values(
 'B등급',80,89.99
);
insert into stu_grade values(
 'C등급',70,79.99
);
insert into stu_grade values(
 'D등급',60,69.99
);
insert into stu_grade values(
 'F등급',0,59.99
);

select * from stu_grade;
select * from stu;
commit;

select no,name,kor,eng,math,total,avg,grade,rank,sdate from students,stu_grade
where total between lototal and hitotal;

select name,total,avg,grade from stu, stu_grade
where avg between loavg and hiavg;

-- stu 성적 등급
update stu a set result = (
select results from (
select no,grade as results from stu, stu_grade
where avg between loavg and hiavg) b
where a.no = b.no
);

commit;

select * from stu;

-- 3. self join
select employee_id,emp_name,manager_id from employees;

select employee_id,emp_name,manager_id from employees where employee_id = 124;

-- self join : 자신의 테이블 2개를 join 결과값을 출력
select a.employee_id,a.emp_name,a.manager_id,b.emp_name from employees a,employees b  where a.manager_id = b.employee_id;
select a.employee_id,a.emp_name,a.manager_id,b.emp_name from employees a,employees b  where a.manager_id = b.employee_id and a.manager_id = 124;


-- 4. outer join
select * from employees,departments
where employees.department_id = departments.department_id(+);  -- (+) : outer join











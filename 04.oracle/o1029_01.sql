-- 테이블 삭제
--drop table member;
--drop table date_tab;
--drop table no_tab;
--drop table students;

-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제
create table member(
 no number(4),
 id varchar2(20),
 pw varchar2(20),
 name varchar2(20),
 phone varchar2(20),
 mdate date
);

-- insert 데이터 입력, update 데이터 수정, delete 데이터 삭제, select 데이터 검색
insert into member values(
 1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);

insert into member values(
 2,'bbb','2222','유관순','010-2222-2222','2024-09-29'
);

select * from member;

commit; 
rollback;

--delete member where no=2;
--delete member;

--update member set name='홍길자' where name='홍길동';
--update member set name='김구';

create table students(
 stuno number(4),
 name varchar2(20),
 kor number(3),
 eng number(3),
 total number(3),
 sdate date
);

-- sysdate 현재날짜,시간 저장
insert into students values(
 1,'홍길동',100,100,100+100,sysdate
);

commit;

-- * 모든 컬럼 검색
select * from students;

-- 특정컬럼을 입력하면 컬럼만 검색
select name, sdate from students;

-- 특정컬럼만 입력하면 컬럼만 입력 / null값은 안 넣는게 좋음(무결점)
insert into students (stuno,name) values(
 2,'유관순'
);

select * from employees;

-- 테이블 복사
create table emp2 as select * from employees;

select * from emp2;

-- 데이터 개수 확인
select count(*) from emp2;

-- 데이터빼고 구조만 복사할 경우 where 1=2;
create table emp3 as select * from employees where 1=2;
select * from emp3;

-- desc 테이블 구조 확인
desc employees;

create table member2 as select * from member where 1=2;

select * from member2;

commit;

-- 테이블이 존재할 경우, 데이터만 복사
insert into member2 select * from member;

--drop table emp3;
desc emp2;

-- 테이블 컬럼데이터 타입, 길이 변경
-- alter 수정 / member테이블 no컬럼의 타입길이 변경
alter table member modify no number(10);

update member set no='';
-- 같은 타입변경 시 제약조건이 없으나, 아예 다른 타입으로 변경 시 데이터가 없어야 함

-- rename 컬럼이름 변경
alter table member rename column no to memberNo;

select * from member;

commit;
desc member;

select employee_id,emp_name,hire_date from employees;

-- 연산자 : 산술연산자 +,-,/,*

--drop table students;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);

select * from students;

-- abs 절대값
select kor,eng,(kor+eng) from students;
select kor,eng,abs(kor-eng) from students;

select * from employees;

commit;

-- 사측연산은 문자열 합치기 제한(concat 또는 ||사용)
--select emp_name+email from employees;
select concat(employee_id,emp_name) from employees;
select employee_id||emp_name from employees;

select salary from employees;
-- 숫자에 ,붙이기(문자로 바꾼후)
select to_char(salary*1384,'999,999,999') from employees;


create table stu(
 no number(4),
 name varchar2(20),
 kor number(3)
);

insert into stu values(1,'홍길동',100);
insert into stu values(2,'유관순',99);

commit;
select * from stu where name is null;

insert into stu values(3,'',0);
insert into stu values(4,null,null);

select * from employees;
select commission_pct from employees;

-- null 아닌 값 출력 : is not null
select commission_pct from employees where commission_pct is not null;

select salary from employees;

select salary, salary*12 from employees;
select salary, salary*12*1384 from employees;

-- 연봉 구하기, 컬럼명 별칭 사용 as ~ / "연 봉"처럼 사이띄우기를 적용하려면 "" 붙여야함(as 생략가능)
select salary, salary*12 as "연 봉",salary*12+(salary*12)*nvl(commission_pct,0)*0.01 as real_yearsalary from employees;

-- nvl(,) 함수 nullvalue : kor값에 null이 있으면 0으로 대체
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu;

select * from students;

select no as 번호,name as 이름,kor 국어,eng 영어,math 수학, total 합계, avg 평균, rank 등수, sdate as 입력일 from students;

select * from employees;
select employee_id||emp_name||email from employees;

select emp_name||' is a '||job_id from employees;

-- 중복제거
select department_id from employees;
select distinct department_id from employees;
-- order by - asc 순차정렬, desc 역순정렬
select distinct department_id from employees order by department_id desc;

select distinct job_id from employees;
select job_id from employees;

-- 문자열자르기 substr

select substr(job_id,0,2) from employees;
select distinct substr(job_id,4) from employees;

-- where절 : 조건에 따른 비교연산자 >,<,>=,<=,=,!=
select * from employees;
select * from employees where manager_id = 124;
select * from employees where job_id = 'SH_CLERK';

select * from employees where employee_id > 100;

select * from students;
select * from students where total >= 250;
select * from students where total >= 250 and kor >= 90;
select * from students where eng >= 70 and eng <= 90 order by eng;

select * from employees;
select * from employees where salary >= 5000 and salary <= 8000 order by salary;

-- <>,^=,!= 다르다(아니다)
select * from employees where salary != 7000;

-- null값은 count에 포함되지 않음
select count(*) from employees where department_id = 50;  -- 45
select count(*) from employees where department_id != 50;  -- 61
select count(*) from employees where department_id is null; -- 1

select count(*) from employees; -- 107
select count(employee_id) from employees;   -- 107개
select count(department_id) from employees; -- 106개, null값 1개 있기 때문에

select employee_id 사원번호,emp_name 사원명,salary 급여 from employees where salary <= 4000 order by salary;

-- 숫자인 경우 비교연산자 가능, 날짜비교연산자 가능
select emp_name,hire_date from employees;
select emp_name,hire_date from employees where hire_date >= '2002/01/01';
select emp_name,hire_date from employees where hire_date <= '1999/12/31';
select emp_name,hire_date from employees where hire_date >= '20010101' and hire_date <= '20041231' order by hire_date;

-- 논리연산자
select * from students;
select count(*) from students where kor >= 90 or eng >= 90;  -- 41
select count(*) from students where kor >= 90 and eng >= 90; -- 3
select count(*) from students where not kor >= 90;


select * from employees;
select * from employees where department_id = 80 and substr(job_id,4) = 'MAN';


select commission_pct from employees where commission_pct is not null;

-- or연산자
select commission_pct from employees where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;
-- in연산자
select commission_pct from employees where commission_pct in (0.2,0.3,0.5);

select employee_id from employees where employee_id = 110 or employee_id = 120 or employee_id = 130;
select employee_id from employees where employee_id in (110,120,130);

select * from employees where employee_id >= 150 and employee_id <= 170;
-- between -and 포함이 되어있는 경우만 해당
select * from employees where employee_id between 150 and 170;


select hire_date from employees;
select hire_date from employees where hire_date in ('2004 02 17', '2002 06 07');

select hire_date from employees;
select hire_date from employees where hire_date between '2002/06/17' and '2004/02/17';

-- MAN으로 끝나는 단어 검색
select hire_date from employees where substr(job_id,4) = 'MAN';

-- like을 활용한
select * from employees where job_id like '%MAN';
select * from employees where job_id like 'ST%';

select * from employees;
select * from employees where emp_name like '%a%';
select count(*) from employees where emp_name like '%a%';

select * from employees;
select * from employees where emp_name like '_t%';

select * from employees where emp_name like '___v%';

select * from employees where emp_name like '%l_';

select * from employees where emp_name like 'D%';


select * from students where no in (10,20,30);

select * from employees where salary >= 4000 and salary <= 8000 order by salary;


select * from member;

update member set id='abc',pw='1111',name='박우정',email='qkrdnwjd0893@naver.com' where id='abc';

commit;

select * from member;

update member set pw='1111' where id='Towell';

----------------------------------------------------------------------------------날짜함수
select sysdate-1,sysdate,sysdate+1 from dual;

select hire_date,round(hire_date,'Month') from employees;

select hire_date,trunc(hire_date,'month') from employees;

select add_months(trunc(sysdate,'month'),1) from dual;

-- vip요금제 변경 다음달 1일부터 혜택
select sysdate,add_months(trunc(sysdate,'month'),1) from dual;

-- 입사일 기준 다음달 1일부터 혜택
select hire_date,add_months(trunc(hire_date,'month'),1) from employees;

-- 입사일 기준 1년 후 날짜, 1년 후 마지막 날 출력
select hire_date,add_months(hire_date,12),last_day(add_months(hire_date,12)) from employees;
select sysdate,sysdate+365,add_months(sysdate,12) from dual;

select hire_date,last_day(hire_date) from employees;

select name,sdate,last_day(sdate+365) from students where last_day(sdate+365) in ('24/08/31','24/09/30','24/10/31','25/08/31','25/09/30','25/10/31');
-- extract : 특정 년,월,일,시,분,초만 분리해서 가져오는 함수
select name,sdate,last_day(sdate+365) from students where extract(month from last_day(sdate+365)) in (8,9,10);

select sysdate from dual;
select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;

select systimestamp from dual;
select extract(hour from systimestamp) from dual;
select extract(minute from systimestamp) from dual;
select extract(second from systimestamp) from dual;

select sdate,extract(month from sdate) from students where extract(month from sdate) in (8,11,12);


select name,sdate,last_day(sdate+365) from students where extract(year from last_day(sdate+365)) = 2025 and extract(month from last_day(sdate+365)) in (8,9,10);

-- substr : 문자에서 시작위치, 가져올 갯수
select sysdate,substr(sysdate,0,2) from dual;
select sysdate,substr(sysdate,4,2) from dual;

select last_day(sdate+365) sdate2 from students where substr(last_day(sdate+365),4,2) in (8,11,12) order by sdate2;

----------------------------------------------------------------------------------형변환함수
-- 날짜 -> 문자 to_char     ## 날짜포맷
-- 문자 -> 날짜 to_date     ## 날짜 사칙연산
-- 숫자 -> 문자 to_char     ## 천단위, 숫자앞에 0 을표시, 통화표시
-- 문자 -> 숫자 to_number   ## 천단위 표시 , 천단위 삭제해서
select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss day') from dual; -- day,dy
select sysdate,to_char(sysdate,'yy-mm-dd hh24:mi:ss dy') from dual; -- hh,hh24
select sysdate,to_char(sysdate,'yy-Mon-dd amhh:mi:ss') from dual; -- am,pm

select hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss') from employees;

select sdate,to_char(sdate,'yyyy/mm/dd') from students;

select kor from students where kor=70;

select salary*1382.86*12 from employees;

-- 숫자 출력 형식
select to_char(salary*1382.86*12,'L999,999,999') from employees;

select 12,to_char(12,'000') from dual;

select to_char(123456,'000000000'),to_char(123456,'999,999,999') from dual;

create table chartable(
    no number(4),
    kor number(10),
    kor_char varchar2(10),
    kor_mark varchar2(10)
);

create table chartable2(
 no number(4),
 kor number(10),
 kor_char number(10),
 kor_mark number(10)
);


insert into chartable values(
 1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);

select * from chartable;

insert into chartable values(
 3,30000,'0030000','3,000,000'
);

-- number str-number넣어도 입력, str
-- 숫자형타입은 숫자앞에 0 있어도 표시되지 않음 : 문자형타입만 가능
insert into chartable2 values(
 3,3000000,0030000,0030000
);

-- 문자형 타입에는 숫자형타입 가능
commit;
-- 숫자형타입, 문자형(숫자) 타입은 사칙연산 가능, 천단위 표시 문자형타입
-- 하지만 문자형 타입(숫자)에 특수문자가 섞여있으면 사칙연산 불가. 천단위표시(999,999,999) 불가
-- 숫자형 다입 + 문자(숫자형) 타입 = 두타입 결과값 출력됨

select * from chartable;
select kor+kor_mark from chartable2;
select kor+kor_char from chartable2;

desc chartable;

-- 문자형타입 -> 날짜형타입 변경
select '20241031','20241031'+2,to_date('20241031')+2 from dual;
select to_date('20241031')+2 from dual;


select to_date('20241031') from dual;

-- number타입 -> 날짜형타입 변경
select sysdate - to_date(20231101) from dual;


-- 천단위 문자형타입 -> 천단위 제외 숫자형타입 변경
select to_number('20,000','999,999') from dual;

select * from chartable;
-- 숫자형타입이기에 사칙연산 가능
select kor,to_number(kor_mark,'999,999,999') from chartable;

commit;

select kor+to_number(kor_mark,'999,999,999') from chartable;

select department_id from employees where department_id is null;
select commission_pct from employees where commission_pct is not null;

select * from employees;
select emp_name,salary,salary+salary*nvl(commission_pct,0) from employees;

-- 숫자형 -> 문자형 변경 후 null : ceo적용
select department_id,nvl(to_char(department_id),'ceo') from employees;

-- 문자, 숫자형 타입 -> 날짜형타입 변경가능
-- 숫자, 날짜형 타입 -> 문자형타입 변경가능
-- 문자형 타입 -> 숫자형타입 변경가능
select 20240101,to_date(20240101) from dual;

-- 날짜형 타입 -> 숫자형타입 변경불가(날짜 -> 문자(형태변형) -> 숫자 순으로 변경해야 함)
--select sysdate,to_number(sysdate) from dual;
select sysdate,to_number(to_char(sysdate,'yyyymmdd')) from dual;

-- 한글로 입력하는 방법
select sysdate,to_char(sysdate,'yyyy"년" mm"월" dd"일" day') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd day') from dual;

---------------------------------------------------------------------------------그룹함수
select salary from employees;
-- sum 합계
select sum(salary) from employees;
select to_char(sum(salary),'999,999') from employees;
-- avg 평균
select avg(salary) from employees;
select round(avg(salary),3) from employees;
select trunc(avg(salary),3) from employees;
-- 최대,최소값  max,min
select max(salary) from employees;
select min(salary) from employees;

-- 평균값 select해서 범위 선택
select count(salary) from employees where salary>=6461.83;
select count(salary) from employees where salary >= (select avg(salary) from employees);

-- emp_name 단일함수, avg(salary) 그룹함수 함께 사용할 수 없음
--select emp_name,avg(salary) from employees;
--select department_id,max(salary) from employees;

select sum(kor),avg(kor),max(kor),min(kor),median(kor) from students;

-- 부서번호가 50인 사원들의 월급 합, 평균, 최대, 최소
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id = 50;

-- 부서번호가 30인 사원들의 월급 합, 평균, 최대, 최소
select sum(salary),avg(salary),max(salary),min(salary) from employees where department_id = 30;
-- 그룹함수&단일함수 함께 사용 / group by로 단일함수를 묶어주면 사용 가능
select department_id,max(salary) from employees group by department_id;

select emp_name,salary from employees;
-- 107명의 평균
select avg(salary) from employees;
-- department_id 부서별 평균
select department_id,round(avg(salary),2),count(salary),max(salary),min(salary) from employees group by department_id;

select count(salary),min(salary),max(salary) from employees where salary >= (select avg(salary) from employees);

---------------------------------------------------------------------------------수학함수
select power(2,3),2*2*2 from dual;

---------------------------------------------------------------------------------문자형함수
--select emp_name,email from employees;
-- 문자형 합치기 || or concat
select emp_name||email from employees;

-- lower 소문자 치환 upper 대문자 치환, initcap 첫글자 대문자 치환
select * from member where name='Bryan';
select * from member where lower(name)='bryan';

select 'joHn',initcap('joHn'),lower('joHn'),upper('joHn') from dual;

-- lpad : 오른쪽 자리수 채우기
select 'john',lpad('john',10,'#') from dual;

-- rpad : 오른쪽 자리수 채우기
select 'john',rpad('john',10,'#') from dual;

-- trim : 앞,뒤 빈공백 없애기, ltrim : 왼쪽공백, rtrim : 오른쪽공백
select '    aaa   ', trim('    aaa   ') from dual;
select length('    aaa   '), length(trim('    aaa   ')) from dual;

-- replace :치환
select '   a  b c  ',trim('   a  b c  '),replace('   a  b c  ',' ','') from dual;

select 'abcdefg',substr('abcdefg',0,3),substr('abcdefg',2,2) from dual;

select emp_name,hire_date from employees where substr(hire_date,4,2) in ('03','08','10');

select emp_name,hire_date from employees where substr(hire_date,4,2) >= 7;

--translate 한번에 여러개 변경 가능
select 'axyz',translate('axyzxbbcyaccx','xy','ab') from dual;
select 'axyz',replace('axyzxbbcyaccx','xy','ab') from dual;

select * from students where length(name) >= 5;

select salary,sum(salary),avg(salary) from employees group by salary;

select eng,sum(eng),avg(eng),min(eng),max(eng) from students group by eng;

select name,to_char(sdate,'"등록일 : "yyyy"년 "mm"월 "dd"일"') from students;
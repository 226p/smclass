--입사일 마지막 날짜 출력

select hire_date,last_day(hire_date) from employees;

-- 1년 이후
select sdate,sdate+365,add_months(sdate,12) from students;

-- 6개월 이내
select sdate,add_months(sdate,-6) from students;

-- 현재일 11/1 기준으로 6개월 이내 가입한 사람들
select sdate from students where sdate>=add_months(sysdate,-6) order by sdate;

-- 결과값을 월별로 그룹핑
select substr(last_day(mdate),1,5) md,count(*) from member group by last_day(mdate) order by md;

select department_id,count(nvl(department_id,0)) from employees group by department_id;

-- 테이블 전체 복사하여 다른 테이블 생성
create table emp3 as select * from employees;
-- 테이블 구조만(데이터없이) 복사하여 다른 테이블 생성
create table emp4 as select * from employees where 1=2;
-- 테이블 구조가 있는 상태에서 다른 테이블의 데이터 복사 후 다른 테이블에 데이터 추가
insert into emp4 select * from employees;

select * from emp4;

rollback;
commit;

-- 제약조건 확인
insert into emp4(emp_name,employee_id,salary,hire_date) select emp_name,employee_id,salary,hire_date from employees;
------------------------------------------------------------------------------------------ 테이블 변경
---- create : 테이블 생성, alter : 테이블 변경, drop : 테이블 삭제

select * from emp4;
---- 테이블 컬럼 추가
alter table emp4 add(hire_date2 date);
---- 테이블 컬럼 변경 : 컬럼 안에 데이터가 있다면 제약조건이 있는지 확인 필수, 컬럼 안 데이터가 null이면 가능
alter table emp4 modify email number(6);
-- 컬럼의 길이 확인
select max(length(emp_name)) from employees;
select length(emp_name) em from employees order by em desc;

-- 데이터 있고 제약조건이 있으면 컬럼 변경 제한
--alter table emp4 modify(emp_name,number(20));

desc emp4;
-- employee_id 값을 email에 복사
update emp4 set email=employee_id;
-- employee_id(숫자형) 값을 phone_number(문자형)에 복사
update emp4 set phone_number = employee_id;

select * from emp4;

commit;

-- 안에 있는 데이터가 모두 숫자형이기 때문에 MANAGER_ID에 복사가능 / 문자가 섞이면 타입변경 불가
update emp4 set MANAGER_ID = PHONE_NUMBER;

rollback;
select * from emp4;
update emp4 set phone_number='198a' where employee_id = 198;


---- 컬럼 이름 변경
desc emp4;
alter table emp4 rename column phone_number to p_number;

-- 속성 변경(제약조건 사라짐)
alter table emp4 modify hire_date date null;
-- 속성 변경(제약조건 설정)
alter table emp4 modify hire_date date not null;

---- 컬럼 삭제
alter table emp4 drop column hire_date2;
---- 테이블 삭제
drop table emp3;
drop table emp2;

---- 테이블 이름변경
rename emp4 to emp44;
------------------------------------------------------------------------------------------ 무결성 제약조건
select * from departments;

drop table bmember;

create table bmember(
 id varchar2(30) primary key,
 pw varchar2(30) not null,
 name varchar2(30) not null,
 nicname varchar2(30),
 age number(3) default 0,
 gender varchar2(6) check(gender in ('male','female')),
 email varchar2(20),
 bdate date default sysdate
);

desc bmember;
-- 입력
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
 'aaa','1111','홍길동','길동스',20,'male','aaa@aaa.com',sysdate
);
insert into bmember(id,pw,name,nicname,gender,email) values(
 'bbb','2222','유관순','관순스','female','bbb@bbb.com'
);
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
 'ccc','3333','이순신','순신스',20,'male','ccc@ccc.com',sysdate
);
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
 'ddd',' ','강감찬','감찬스',20,'male','ddd@ddd.com','2024/01/01'
);
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values(
 'eee','555','김구','김구스',20,'male','eee@eee.com','2024/01/01'
);

select * from bmember;

create table emp3(
 empno number(4) unique,
 ename varchar2(30) not null,
 job varchar2(30),
 deptno number(2)
);

rollback;
insert into emp3 values(
 1,'홍','01','01'
);
insert into emp3 values(
 2,'유','02','02'
);
insert into emp3(ename,job,deptno) values(
 '이','03','03'
);
insert into emp3 values(
 4,'강','04','04'
);

select * from emp3;

desc member;

-- primary key 추가, 설정 시 null값, 중복이 존재하면 안됨
-- constraint id_pk 이름설정
alter table member add constraint id_pk primary key (id);
-- primary key 삭제
alter table member drop constraint id_pk;
select * from member;

--insert into member values(
-- 'aaa','1111','홍길자','aaa@aaa.com','123-456-7890','Female','golf',sysdate
--);

create table board(
 bno number(4) primary key,
 btitle varchar2(100) not null,
 bcontent clob,
 id varchar2(30),
 bgroup number(4),
 bindent number(4),
 bstep number(4),
 bhit number(4),
 bdate date,
 bfile varchar2(100)
);

drop table board;

insert into board values(
 board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,0,sysdate,''
);
insert into board values(
 board_seq.nextval,'제목2','내용2','bbb',board_seq.currval,0,0,0,sysdate,''
);


insert into board values(
 board_seq.nextval,'제목5','내용5','ddd',board_seq.currval,0,0,0,sysdate,''
);

commit;

select * from board;

create table mem2 (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);

drop table mem2;


select * from mem2;

commit;

update mem2 set id='abc',pw='1111',name='박우정',email='qkrdnwjd0893@naver.com' where id = 'Trineman';

--insert into member select * from mem2;

select * from member;

select * from board;
select * from bmember;

-- 관계형db(테이블 조인) : 두 테이블을 합친 후 결과를 한번에 출력, 중복되는 것을 방지해줌
-- member id : primary key, board id : foreign key
select bno,btitle,bcontent,nicname,email,bgroup,bstep,bhit,bindent,bfile from board, bmember where board.id=bmember.id;

select employee_id,emp_name,email,salary,employees.department_id,department_name
from employees,departments
where employees.department_id=departments.department_id;


select department_id,department_name from departments where department_id=50;



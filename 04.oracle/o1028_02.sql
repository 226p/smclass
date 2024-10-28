-- 검색 select *
-- select * from employees;

-- 테이블 생성
create table students (
no number(4),
name varchar2(20),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(10),
rank number(4)
);

-- 테이블 삭제
--drop table students;   

-- 데이터 입력
insert into students (no,name,kor,eng,math,total,avg,rank) values(
 1,'홍길동',100,100,99,299,(299/3),1
);

insert into students (no,name,kor,eng,math,total,avg,rank) values(
 2,'유관순',100,90,99,289,(289/3),1
);

-- 테이블 검색
select no,name,kor,eng,math,total,avg,rank from students;

-- 데이터 확정 : commit, rollback
commit;
rollback;

select * from students;

commit;

-- 가로줄 row(필드), 세로줄 col
select * from employees;

create table member(
id varchar2(20) primary key,
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

insert into member (id,pw,name,phone) values(
 'aaa','1111','홍길동','010-1111-1111'
);

select * from member;

commit;

insert into member values(
'bbb','2222','유관순','010-2222-2222'
);

commit;

insert into member(id,name) values(
 'ccc','이순신'
);

select * from member;

select id,phone from member;

select name,phone from member;

select * from employees;

select emp_name,salary from employees;

select * from employees;

select * from member;

-- 데이터 수정
update member set name='홍길자' where id='aaa';

select * from member;

-- 데이터 삭제
delete member where id='ccc';

commit;

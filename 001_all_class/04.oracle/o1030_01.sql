-- dual 가상(임시)테이블
select sysdate from dual;

select sysdate-30,sysdate,sysdate+30 from dual;

-- employees테이블 hire_date 컬럼
-- 날짜도 사측연산됨
select hire_date+1,hire_date,hire_date-1 from employees;

-- 날짜 범위 검색가능, order by 정렬(asc:순차정렬, desc:역순정렬)
select emp_name,hire_date from employees where hire_date>='02/01/01' and hire_date<='04/12/31' order by hire_date desc;

select emp_name,hire_date from employees where hire_date between '02/01/01' and '04/12/31' order by hire_date;

-- like / 와일드카드 % 글자가 들어갔는지, _ 몇번째 글자에 있는지
select emp_name from employees where emp_name like '___a%';
select emp_name from employees where emp_name like '%a_';

select department_id from employees order by department_id desc;
select emp_name,salary from employees order by salary desc;

select name,total from students order by total desc;

select emp_name,hire_date from employees order by hire_date;

-- 두 가지 역순정렬(kor기준 역순정렬, 그후 같은 숫자일 때 eng도 역순정렬)
select name,kor,eng,math from students order by kor desc, eng desc;

-- 문자정렬
select name from students order by name desc;
select emp_name,hire_date from employees order by hire_date, emp_name desc;

-- 숫자함수 : dual 가상(임시)테이블
select -10 val,abs(-10) abs from dual;

-- 숫자함수: abs 절대값, round 반올림, seil 올림, floor 버림, power(m,n) m의n승
select kor,kor-eng,abs(kor-eng) abs from students order by abs desc;
select 3.141592, floor(3.141592) from dual;
select 34.5678,round(34.5678) from dual;
-- 둘째자리까지 출력(셋째자리에서 반올림)
select 34.5678,round(34.5678,2) from dual;
-- 양수 첫째자리에서 반올림(소수점 자리수에서 앞쪽으로 한칸위치 반올림)
select 34.5678,round(34.5678,-1) from dual;

select 34.5678,floor(34.5678) from dual;
select 34.5678,trunc(34.5678,2) from dual;
select 34.5678,ceil(34.5678) from dual;

select 27/2,mod(27,2) from dual;
select 31/7,mod(31,7) from dual;


select * from employees;

select emp_name,employee_id from employees where mod(employee_id,2) != 0 order by employee_id;


-- 최종연봉 : 월급*12+(월급*12)*커미션
select emp_name,salary,round((salary*12+(salary*12)*nvl(commission_pct,0))*1381.86795) ysalary from employees;
select commission_pct from employees where commission_pct is not null;

-- 쿼리문
select * from students;
---------------------------------------------------------------시퀀스
-- 시퀀스 : 중복없이 자동으로 번호를 부여
create sequence stu_seq
start with 1 -- 시작번호
increment by 1 -- 증가되는 텀
minvalue 1
maxvalue 9999
nocycle
nocache;

-- 시퀀스에서 번호생성
select stu_seq.nextval from dual;
-- 시퀀스 생성 확인
select stu_seq.currval from dual;

-- 게시판 테이블 생성
create table board(
 bno number(4),
 btitle varchar2(100),
 bcontent varchar2(4000),  -- varchar2 최대 4000 / 한글 1글자에 3byte
 bid varchar2(30),
 bhit number(10),
 bdate date
);

insert into board values(
 2,'제목입니다.2','내용입니다.2','bbb',1,sysdate
);

insert into board values(
 board_seq.nextval,'제목입니다.','내용입니다.','aaa',1,sysdate
);

select * from board;

commit;

create sequence board_seq
start with 9   -- 시작번호
increment by 1 -- 증감되는 텀
minvalue 1     -- 최소값
maxvalue 9999  -- 최대값
nocycle        -- cycle : 1-9999이상이 되면 다시 1로 돌아감
nocache;       -- cache : 메모리에 시퀀스값 미리할당

insert into board values(
 board_seq.nextval,'제목입니다.','내용입니다.','aaa',1,sysdate
);

update board set btitle='제목을 다시 변경' where bno=8;

drop table board;

create table board(
 bno number(4),
 btitle varchar2(100),
 bcontent clob,  -- clob 대용량 글자타입
 bid varchar2(20),
 bgroup number(4),  -- 답변달기 그룹핑
 bstep number(4),  -- 답변달기 경우 순서정의
 bindent number(4), -- 답변달기 들여쓰기
 bhit number(10),   -- 조회수
 bdate date         -- 등록일
);


insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate
);

select * from board;


create sequence student_seq
start with 101
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

delete students where name='홍길순';

select * from students;

insert into students values(
student_seq.currval,'홍길순',99,99,90,99+99+90,round((99+99+90)/3,3),0,sysdate
);

select no,name,kor,eng,math,total,round(avg,2),rank,sdate from students;

select s.*,round(avg,2) from students s;

rollback;

--select dept_seq.nextval from dual;

create sequence s_seq
start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

select emp_seq.nextval from dual;

--drop sequence s_seq;

-- 문자형 : char, varchar2, nchar, nvarchar2, long(구형), clob(최신)
-- char : 한글문자 입력시 3byte 사용
-- nvarchar2(5) : 한글문자를 5자리까지 입력가능 2byte
-- 숫자형 : number
-- 날짜형 : date,timestamp
-- date : 초까지 입력 timestamp : 밀리세컨드까지 입력

select '홍길동' from dual;
select length('홍길동') from dual;
select lengthb('홍길동') from dual;

-- 이름의 길이로 정렬(별칭을 줌으로써)
select name,length(name) n from students order by n;

-- 합계>=200, 10<=번호<=50, 이름에 두번째자리에 e가 들어간 학생 출력
select * from students;
select * from students where total >= 200 and no >= 1 and no <= 50 and name like '_e%';

select * from students where total>=200;

-- 2중 쿼리문
select * from (
select * from students where total>=200
) where name like '_e%' and no>=30;

rollback;

select * from students;
select no,name,total,rank from students;

-- 등수함수 : rank() over(기준점)
-- select rank() over(order by total desc); 중복없음 = 유일키,기본키, 프라이머리키
select no,name,total,rank() over(order by total desc) rank from students;
select ranks from (select no,rank() over(order by total desc) ranks from students);

-- 수정 : update
update students a 
set rank = (select ranks from (select no,rank() over(order by total desc) ranks from students) b
where a.no = b.no);

update students a 
set rank = 1
where a.no = 101;

select * from students order by rank;

commit;

select no,rank() over(order by total desc) ranks from students;

update students set rank = 1 where no = 101;
update students set rank = 2 where no = 96;
update students set rank = 2 where no = 64;
update students set rank = 4 where no = 49;
update students set rank = 5 where no = 14;

-- employees 복사하여 emp2 생성
create table emp2 as select * from employees;


-- 테이블 rank 컬럼 추가
alter table emp2 add rank number(4);

-- rank() 등수부여 출력
select emp_name,employee_id,rank() over(order by employee_id desc) ranks from emp2;

-- rank() 등수를 rank에 입력
update emp2 e
set rank = (select ranks from (select employee_id,rank() over(order by employee_id desc) ranks from emp2) e2
where e.employee_id = e2.employee_id
);

select emp_name,employee_id,rank from emp2 order by rank;

commit;

-- rank 컬럼을 emp_name뒤에 배치(숨김처리 후 보이게하면 옮겨짐)
alter table emp2 modify email invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify MANAGER_ID invisible;
alter table emp2 modify COMMISSION_PCT invisible;
alter table emp2 modify RETIRE_DATE invisible;
alter table emp2 modify DEPARTMENT_ID invisible;
alter table emp2 modify JOB_ID invisible;
alter table emp2 modify CREATE_DATE invisible;
alter table emp2 modify UPDATE_DATE invisible;

-- 다시 보이게
alter table emp2 modify email visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify hire_date visible;
alter table emp2 modify salary visible;
alter table emp2 modify MANAGER_ID visible;
alter table emp2 modify COMMISSION_PCT visible;
alter table emp2 modify RETIRE_DATE visible;
alter table emp2 modify DEPARTMENT_ID visible;
alter table emp2 modify JOB_ID visible;
alter table emp2 modify CREATE_DATE visible;
alter table emp2 modify UPDATE_DATE visible;

-- 다시 원상복구
alter table emp2 modify rank invisible;
alter table emp2 modify rank visible;

select * from emp2 order by rank;

-- 테이블 rank 컬럼 추가
alter table emp2 add rank number(4);

desc emp2;
-- 컬럼 삭제
alter table emp2 drop column email;
alter table emp2 drop column phone_number;

alter table emp2 drop column hire_date;
alter table emp2 drop column SALARY;
alter table emp2 drop column COMMISSION_PCT;
alter table emp2 drop column RETIRE_DATE;
alter table emp2 drop column CREATE_DATE;
alter table emp2 drop column UPDATE_DATE;

-- 부서명 없음
select * from emp2;

select * from departments;
desc departments;

-- 부서명 departments
alter table emp2 add department_name varchar2(80);

select department_id,department_name from emp2;
select department_id,department_name from departments;

-- 부서명 입력
update emp2 e
set e.department_name = (select d from (select department_id,department_name d from departments) e2 
where e.department_id = e2.department_id);

select * from emp2;

commit;

create table stu2 as select * from students;

alter table stu2 drop column total;

select * from stu2;

commit;

alter table stu2 add total number(3);
alter table stu2 add avg number(3);
alter table stu2 add rank number(3);

alter table stu2 modify sdate invisible;
alter table stu2 modify sdate visible;

update stu2 set total = kor+eng+math, avg = round((kor+eng+math)/3,2);


select no,rank() over(order by total desc) from stu2;

update stu2 s
set rank = (select r from(select no,rank() over(order by total desc) r from stu2) r2
where s.no = r2.no
);

---- 날짜 함수
select sysdate from dual;
select sysdate-1 from dual;
select sysdate+30 from dual;

create table datetable (
no number(4),
predate date,
today date,
nextdate date
);

insert into datetable values(
 1,sysdate-30,sysdate,sysdate+180
);

select no,predate,today 가입일, nextdate 만료일 from datetable;
select * from datetable;


select * from member;

select id,name,sysdate,round(sysdate-mdate) from member;
select id,name,sysdate,round(sysdate-mdate) from member where sysdate >= mdate+180;


---------------------------------------------------------------날짜함수
select * from employees;

select emp_name,hire_date,round(sysdate-hire_date) from employees;

-- 15일 이상이면 한달 올림, 15일 미만이면 일을 초기화 
select emp_name,hire_date,round(hire_date,'month') from employees;

-- 초기화
select emp_name,trunc(hire_date,'month'),hire_date from employees;

-- 입사일 & 현재일 기준의 달수
select emp_name,sysdate,months_between(sysdate,hire_date) from employees;
-- months_between : 두 일자 가운데 지나간 달수를 알려줌
select hire_date,sysdate,round(months_between(sysdate,hire_date)) 달수, round(sysdate-hire_date) 일수 from employees;

-- add_months : 3개월 추가
select hire_date,add_months(hire_date,3) from employees;
-- next_day : 다음주 요일 날짜를 알려줌
select next_day(sysdate,'수요일') from dual;
-- last_date : 그 달의 마지막 날짜를 알려줌
select hire_date, last_day(hire_date) from employees;

select sysdate,last_day(sysdate) from dual;


---------------------------------------------------------------형변환 함수
select sysdate from dual;
select to_char(sysdate,'yyyy/mm/dd hh:mi:ss') from dual;
-- 입력타입은 날짜형이 되어야 함.
select to_char(to_date('24/01/01'),'yyyy-mm-dd') from dual;



select * from member where id='aaa' and pw='1111';

update member set id='abc', pw='1111', name='박우정',email='qkrdnwjd0893@naver.com',gender='Female' where id='Trineman';

select * from member;

commit;






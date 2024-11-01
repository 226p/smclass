desc board;

-- bmember 테이블 id, foreign key로 board, board2에 등록
-- 닉네임 : id_fk, foreign key(외래키) : id, bmember테이블의 primary key(기본키) : id 등록
-- 원본의 primary key데이터 지우려면, 원칙적으로 foreign key의 데이터 모두 삭제해야 삭제됨
-- foreign key 해체해야 삭제됨
alter table board add constraint id_fk foreign key(id) references bmember(id);

select * from board;

select * from bmember;

-- abc 글에 등록하면 등록이 안됨
alter table board drop constraint id_fk;

insert into board values(
 board_seq.nextval,'제목6','내용6','abc',board_seq.currval,0,0,0,sysdate,''
);


delete board where bno=7;

commit;
-- 테이블 create할 때, foreign key 생성
create table board2(
 bno number(4) primary key,
 btitle varchar2(1000) not null,
 bcontent clob,
 id varchar2(30),
 constraint id_fk foreign key(id) references bmember(id)
);

select * from bmember;

rollback;
delete bmember where id='aaa';
delete board where id='aaa';

-- foreign key로 등록이되면, primary key 삭제할 때 foreign key에 데이터가 있으면 삭제불가
-- on delete cascade : primary key가 삭제되면, foreign key로 등록된 모든 글을 삭제시킴
alter table board add foreign key (id) references bmember(id) on delete cascade;

--alter table board constraint id_fk foreign key (id) references bmember(id) on delete cascade;

rollback;


create table emp02(
 empno number(4) primary key,
 ename varchar2(30) default '무명',
 income number(4) default 0,
 salary number(7,2) check(salary between 2000 and 20000),
 gender varchar2(10) check(gender in('Male','Female')),
 edate date default sysdate
);

-- check가 지정되어 있는 컬럼에 추가
insert into emp01 values(
 1,'홍길동',2500,'Male'
);
-- salary 범위를 벗어나면 에러, male,female 이외 단어 입력시 에러
insert into emp01 values(
 2,'유관순',200,'Female'
);
insert into emp01 values(
 3,'이순신',200,'male'
);

insert into emp02 (empno,salary,gender) values(
1,5000,'Male'
);

select * from emp02;

commit;


drop table chartable2;

-- 기본값 : 입력하지 않을시, 자식데이터가 있을경우 부모데이터 삭제불가

-- 1. on delete resticited(기본값)(ex) 네이버카페 인원이 1명이라도 있으면 카페 삭제 불가능)
-- 자식데이터가 있을 경우 부모데이터 삭제불가
delete bmember where bno=3;
delete bmember where id='aaa';
rollback;

-- 2. on delete cascade(ex) 네이버 카페 탈퇴시, 블로그, 카페 접속 제한)
--부모데이터 삭제 시, 자식데이터 모두 삭제
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete cascade;

-- 3. on delete set null
--부모데이터 삭제 시, 자식데이터에 해당하는 값 null표시
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete set null;


create table mem(
 id varchar2(30) primary key,
 pw varchar2(30) not null,
 name varchar2(30) default '무명',
 age number(3) default 0,
 birth date,
 gender varchar2(6) check(gender in ('Male','Female')),
 hobby varchar2(50) default 'game',
 mdate date default sysdate
);


insert into mem values(
 'aaa','1111','홍길동','24','2000/05/05','Male','golf',sysdate
);
insert into mem values(
 'ccc','1111','이순신','23','2001/07/25','Male','game',sysdate
);

commit;

select * from employees;

select count(*) person,department_id from employees where department_id='50' group by department_id;

-- 부서별 인원수 : employees 부서번호, departments 부서이름 가져오기
select count(*) no,a.department_id dept,department_name dept_name
from employees a, departments b 
where a.department_id=b.department_id and a.department_id=50
group by a.department_id,department_name;

select * from mem;

rollback;

insert into mem(id,pw,name,age,birth,gender,hobby) values ('ddd','1111','강감찬',22,'20020312','Male','game');

alter table students modify sdate date default sysdate;
alter table students modify rank number(3,0) default 0;




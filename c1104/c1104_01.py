import oracledb

# db 연결함수
def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try : conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e : print("예외처리 :",e)
  return conn

# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students테이블 사용해서
# 시퀀스 students_seq 생성
# 번호,김유신,99,98,96 합계,평균,등수,입력일
### 시작 ###
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','날짜']

while True:
  print("[ 학생성적프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 검색")
  print("4. 학생성적 정렬")
  print("5. 등수처리")
  print("0. 프로그램 종료")
  print()
  choice = input("원하는 번호를 입력하세요. >>")

  if choice == '1':
    conn = connects()
    cursor = conn.cursor()
    sql = "select max(no) from students"
    cursor.execute(sql)
    row = cursor.fetchone()
  
    print("[ 학생성적 입력 ]")
    no = row[0]
    name = input(f"{no}학생 이름을 입력하세요. >> ")
    kor = int(input("국어점수를 입력하세요. >> "))
    eng = int(input("영어점수를 입력하세요. >> "))
    math = int(input("수학점수를 입력하세요. >> "))
    total = kor+eng+math
    avg = total/3

    s_list = [name,kor,eng,math,total,avg]
    sql = 'insert into students (no,name,kor,eng,math,total,avg) values (students_seq.nextval,:1,:2,:3,:4,:5,:6)'
    cursor.execute(sql,s_list)
    conn.commit()
    print(f"{name} 학생의 정보가 저장되었습니다.")
    print()
    cursor.close()

  elif choice == '2':
    print("[ 학생성적 출력 ]")

    conn = connects()
    cursor = conn.cursor()
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for s in s_title:
      print(s,end='\t')
    print()
    print("-"*80)
    if len(rows)<1 :
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end='\t')
      print()
    print()
    print("모든 학생의 정보가 출력되었습니다.")
    print()
    
    conn.close()
    
  elif choice == '3':
    print("[ 학생성적 검색 ]")
    print("1. 이름으로 검색")
    print("2. 합계로 검색")
    choice = input("원하는 번호를 입력하세요. >> ")
    if choice == '1':
      name = input("성적을 출력할 학생의 이름을 입력하세요. >> ")
      search = '%'+name+'%'
      conn = connects()
      cursor = conn.cursor()
      sql = 'select * from students where name like :search'
      cursor.execute(sql,search=search)

      rows = cursor.fetchall()
      print(f"{len(rows)}명의 학생 정보가 검색되었습니다.")
      for row in rows:
        print(row)
      print()
      conn.close()

  elif choice == '4':
    print("[ 학생성적 정렬 ]")
    print("1. 이름 순차 정렬(a,b,c...ㄱ,ㄴ,ㄷ..)")
    print("2. 이름 역순 정렬(ㅎ,ㅍ,ㅋ..z,y,x)")
    print("3. 합계 순차 정렬(높은 점수 순)")
    print("4. 합계 역순 정렬(낮은 점수 순)")

    choice = input("원하는 정렬 방식 번호를 입력하세요. >> ")
    if choice == '1':
      conn = connects()
      cursor = conn.cursor()
      sql = 'select * from students order by name'
      cursor.execute(sql)
      
      rows = cursor.fetchall()
      for row in rows:
        print(row)
      print()
    elif choice == '2':
      conn = connects()
      cursor = conn.cursor()
      sql = 'select * from students order by name desc'
      cursor.execute(sql)
      rows = cursor.fetchall()

      for row in rows:
        print(row)
      print()
    elif choice == '3':
      conn = connects()
      cursor = conn.cursor()
      sql = 'select * from students order by total desc'
      cursor.execute(sql)
      rows = cursor.fetchall()

      for row in rows:
        print(row)
      print()
    elif choice == '4':
      conn = connects()
      cursor = conn.cursor()
      sql = 'select * from students order by total'
      cursor.execute(sql)
      rows = cursor.fetchall()

      for row in rows:
        print(row)
      print()
    
  elif choice == '5':
    print("[ 등수처리 ]")
    conn = connects()
    cursor = conn.cursor()
    sql = 'update students a set rank = (select ranks from (select no,rank() over(order by avg desc) ranks from students) b where a.no = b.no)'
    cursor.execute(sql)
    conn.commit()

    sql = 'select * from students order by rank'
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
      print(row)
    print()

  elif choice == '0':
    print("프로그램을 종료합니다.")
    break 





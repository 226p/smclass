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

while True:
  print("[ 학생성적프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 검색")
  print("0. 프로그램 종료")
  print()
  choice = input("원하는 번호를 입력하세요. >>")

  if choice == '1':
    conn = connects()
    cursor = conn.cursor()
    sql = "select students_seq.currval from dual"
    cursor.execute(sql)
    row = cursor.fetchone()
  
    print("[ 학생성적 입력 ]")
    no = 0
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
    print(f"{name} 학생의 정보가 입력되었습니다.")
    print()
    conn.close()

  elif choice == '2':
    print("[ 학생성적 출력 ]")

    conn = connects()
    cursor = conn.cursor()
    sql = 'select * from students'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
      print(row)
    print("모든 학생의 정보가 출력되었습니다.")
    print()
    
    conn.close()
    
  elif choice == '3':
    print("[ 학생성적 검색 ]")
    name = input("성적을 출력할 학생의 이름을 입력하세요. >> ")

    conn = connects()
    cursor = conn.cursor()
    sql = 'select * from students where name=:name'
    cursor.execute(sql,name=name)
    row = cursor.fetchone()
    print(f"{name} 학생의 정보가 검색되었습니다.")
    print(row)
    print()
    
  elif choice == '0':
    print("프로그램을 종료합니다.")
    break 





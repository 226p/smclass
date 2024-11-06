import oracledb
import func
import datetime

nowYear = datetime.datetime.now().year

def connects():  ### db연결 함수
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리 :",e)
  return conn


def member_count():
  conn = connects()
  cursor = conn.cursor()
  # sql = "select count(*) no,a.department_id dept,department_name dept_name from employees a, departments b where a.department_id=b.department_id and a.department_id=50 group by a.department_id,department_name"
  sql = "select count(*) from mem"
  cursor.execute(sql)
  row = cursor.fetchone()
  conn.close()
  return row[0]



all_member = member_count()
print("[ 커뮤니티 ]")
print(f"현재 회원수 : {all_member}")
print("1. 로그인")
print("2. 회원가입")
print("3. 회원정보 수정")
print("0. 프로그램 종료")
print("-"*30)
choice = input("원하는 번호를 입력하세요. >> ")

if choice == '2':
  print("[ 회원가입 ]")
  user_id = input("아이디를 입력하세요. >> ")
  user_pw = input("비밀번호를 입력하세요. >> ")
  name = input("이름을 입력하세요. >> ")
  birth = input("생년월일을 입력하세요.(ex ) 20020312) >> ")
  age = nowYear-int(birth[:4])   # 나이 자동계산
  gender = input("성별을 입력하세요. (Male,Female)>> ")
  hobby = input("취미를 입력하세요. >> ")

  my_list = [user_id,user_pw,name,age,birth,gender,hobby]

  conn = connects()
  cursor = conn.cursor()
  sql = "insert into mem (id,pw,name,age,birth,gender,hobby) values (:1,:2,:3,:4,:5,:6,:7)"
  cursor.execute(sql,my_list)
  # sql = "insert into mem (id,pw,name,age,birth,gender,hobby) values (:id,:pw,:name,:age,:birth,:gender,:hobby)"
  # cursor.execute(sql,id=user_id,pw=user_pw,name=name,age=age,birth=birth,gender=gender,hobby=hobby)
  conn.commit()
  conn.close()

elif choice == '3':
  print("[ 회원정보 수정 ]")
  conn = connects()
  cursor = conn.cursor()
  user_id = 'aaa'
  sql = "select * from mem where id=:id"
  cursor.execute(sql,id=user_id)
  row = cursor.fetchone()
  print("현재정보 hobby :", row[6])

  hobby = input("수정할 취미를 입력하세요. >> ")

  sql = "update mem set hobby=:hobby where id=:id"
  cursor.execute(sql,hobby=hobby,id=user_id)
  conn.commit()
  conn.close()


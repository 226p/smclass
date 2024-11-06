import oracledb
import random
import smtplib
from email.mime.text import MIMEText
import func

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
  sql = "select count(*) from mem"
  cursor.execute(sql)
  row =cursor.fetchone()
  print(row)
  cursor.close()
  return row[0]

### 회원수 확인값 리턴
all_member = member_count()
def screen():  ### 시작화면 함수선언
  print("[ 커뮤니티 ]")
  print(f"현재 회원수 : {all_member}")
  print("1. 로그인")
  print("2. 회원가입")
  print("3. 회원정보 수정")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요. >> ")
  return choice


def memLogin():  ### 로그인 함수
  print("[ 로그인 ]")
  user_id = input("아이디를 입력하세요. >> ")
  user_pw = input("비밀번호를 입력하세요. >> ")

  ## db접속
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from mem"
  cursor.execute(sql,id=user_id,pw=user_pw)
  row =cursor.fetchone()
  cursor.close()
  if row == None:
    print("로그인에 실패하였습니다. 아이디 또는 비밀번호를 확인해주세요.")
    return
  print(f"로그인을 성공하였습니다. {row[2]} 님 환영합니다. ")
  print()


def search_pw():  ### 비밀번호 찾기 함수
  print("[ 비밀번호 찾기 ]")
  search = input("아이디를 입력하세요. >> ")
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from member where id=:id"
  cursor.execute(sql,id=search)
  row = cursor.fetchone()

  if row == None:
    print("아이디가 존재하지 않습니다. 회원가입을 해주십시오.")
    return
  input("아이디를 확인했습니다. 임시 비밀번호를 발급합니다. enter키>>")

  random_pw = func.emailSand(row[3])
  # 임시비밀번호 업데이트
  sql = "update member set pw=:pw where id=:id"
  cursor.execute(sql,pw=random_pw,id=search)
  conn.commit()
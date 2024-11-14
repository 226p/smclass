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


def random_pw():  ### 랜덤비밀번호 발급 함수
  a = random.randrange(0,10000) # 0-9999
  ran_num = f"{a:04}"
  return ran_num


def emailSand(email):  ### 이메일 비밀번호 발송 함수
  #email 발송
  smtpName = "smtp.naver.com"
  smtpPort = 587

  sendEmail = 'qkrdnwjd0893@naver.com'
  pw = "7VZNPVDYKYRK"
  recvEmail = email

  ran_num = random_pw()

  title = '[ 메일발송 ] 임시 비밀번호 발급 안내'
  content = ran_num
  content = "임시 비밀번호 : "+content

  # 설정
  msg = MIMEText(content)
  msg['Subject'] = title
  msg['From'] = sendEmail
  msg['To'] = recvEmail

  # 서버이름,서버포트
  s = smtplib.SMTP(smtpName,smtpPort)
  s.starttls()
  s.login(sendEmail,pw)
  s.sendmail(sendEmail,recvEmail,msg.as_string())
  s.quit()

  print("메일 발송 완료")
  return ran_num


def screen():  ### 시작화면 함수선언
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
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
  sql = "select * from member where id=:id and pw=:pw"
  cursor.execute(sql,id=user_id,pw=user_pw)
  row =cursor.fetchone()
  conn.close()
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
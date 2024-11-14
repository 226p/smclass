import oracledb
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외발생 :",e)
  return conn

while True:
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
  print("0. 프로그램 종료")
  print()
  choice = input("원하는 번호를 입력하세요. >> ")

  if choice == '1':
    print("[ 로그인 ]")
    user_id = input("아이디를 입력하세요. >>")
    user_pw = input("비밀번호를 입력하세요. >>")

    conn = connects()  # db접속
    cursor = conn.cursor()
    sql = "select * from member where id=:id and pw=:pw"
    cursor.execute(sql,id=user_id,pw=user_pw)
    row = cursor.fetchone()
    # print(row)
    if row != None : print(f"{row[2]} 님 로그인을 성공했습니다.")
    else: print("아이디 또는 비밀번호가 일치하지 않습니다.")
    cursor.close()

    print("[ 학생성적프로그램에 접속합니다. ]")
    ### 프로그램 구현

  elif choice == '2':
    print("[ 비밀번호 찾기 ]")
    search = input("해당 아이디를 입력하세요. >> ")
    # 아이디 유무 확인
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id"
    cursor.execute(sql,id=search)
    row = cursor.fetchone()
    if row != None:
      print("아이디가 존재합니다. 임시 비밀번호를 발급합니다.")
      # 임시 비밀번호 생성 & member테이블에 적용
      a = random.randrange(0,10000)  # 0-9999
      ran_num = f"{a:04}"
      sql = "update member set pw=:pw where id=:id "
      cursor.execute(sql,pw=ran_num,id=search)
      conn.commit()

      # print("파일이 수정되었습니다.")
      # 이메일로 임시 비밀번호 전송
      smtpName = "smtp.naver.com"
      smtpPort = 587

      # id, pw, 받는사람이메일주소
      sendEmail = "qkrdnwjd0893@naver.com"
      pw1 = "7VZNPVDYKYRK"
      recvEmail = f"{row[3]}"

      title = "제목 : 커뮤니티 임시 비밀번호 발급 안내"
      content = f"◟(ᵔ ̮ ᵔ)͜   ♡ 당신의 임시 비밀번호 : {ran_num}"

      # 설정
      msg = MIMEText(content)
      msg['Subject'] = title
      msg["From"] = sendEmail
      msg['To'] = recvEmail
      print("msg 데이터 : ",msg.as_string())

      # 서버이름,서버포트
      s = smtplib.SMTP(smtpName,smtpPort)
      s.starttls()  # 보안연결
      s.login(sendEmail,pw1)
      s.sendmail(sendEmail,recvEmail,msg.as_string())
      s.quit()
      # 메일발송 완료
      print("임시비밀번호를 가입한 메일로 발송하였습니다. 다시 로그인하세요.")
    else:
      print("아이디가 존재하지 않습니다. 회원가입을 해주십시오.")
    cursor.close()

  elif choice == '3':
    print("[ 회원가입 ]")


  elif choice == '0':
    print("프로그램을 종료합니다.")
    break


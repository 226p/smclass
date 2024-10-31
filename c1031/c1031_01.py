import oracledb
import random
import smtplib
from email.mime.text import MIMEText
import func


while True:
  ## 로그인이 되어 있지 않은 상태
  choice = func.screen()

  ## 로그인 성공한 상태 --> 학생성적 프로그램 가동
  # print("[ 학생성적 프로그램 ]")
  # print("1. 학생성적 입력")
  # print("2. 학생성적 출력")
  # print("3. 학생성적 수정")
  # print("0. 로그아웃")

  # 로그인 부분
  if choice == '1':
    func.memLogin()
    
  # 비밀번호 찾기 부분  
  elif choice == '2':
    func.search_pw()

  # 회원가입 부분
  elif choice == '3':
    pass
  
  elif choice == '0':
    print("프로그램을 종료합니다.")
    break





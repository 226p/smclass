import oracledb
import random
import smtplib
from email.mime.text import MIMEText
import func


all_member = func.member_count()

print("[ 커뮤니티 ]")
print(f"현재 회원수 : {all_member}")
print("1. 로그인")
print("2. 회원가입")
print("3. 회원정보 수정")
print("0. 프로그램 종료")
print("-"*30)
choice = input("원하는 번호를 입력하세요. >> ")

while True:
  ## 로그인이 되어 있지 않은 상태
  choice = func.screen()

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





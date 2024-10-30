import random
import oracledb

# 랜덤 4자리 숫자 발급
# a_list = [0,1,2,3,4,5,6,7,8,9]
a = random.randrange(0,10000)  # 0-9999
ran_num = f"{a:04}"
print(ran_num)
#----------------------------------------------------------------
# 데이터 수정
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
  print("-"*30)
  choice = input("원하는 번호를 입력하세요. >> ")

  if choice == '1':
    print("[ 로그인 ]")
    user_id = input("아이디를 입력하세요. >>")
    user_pw = input("비밀번호를 입력하세요. >>")

    conn = connects()  # db접속
    cursor = conn.cursor()
    sql = "update member set pw=:pw where id=:id "
    cursor.execute(sql,pw=user_pw,id=user_id)
    conn.commit()

    print("파일이 수정되었습니다.")
    cursor.close()

    print("[ 학생성적프로그램에 접속합니다. ]")
    ### 프로그램 구현






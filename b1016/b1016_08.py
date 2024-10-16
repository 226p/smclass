import datetime

member = []              # member.txt
m_keys = ["id","pw","name","nickName","money","address"]

f = open("member.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(",")
  m[4] = int(m[4])
  member.append(dict(zip(m_keys,m)))

cart = []              # cart.txt
c_keys = ["cNo","id","name","pCode","pName","price","date"]

ff = open("cart.txt","r",encoding="utf-8")
while True:
  line = ff.readline()
  if not line: break
  c = line.strip().split(",")
  c[0] = int(c[0])
  c[5] = int(c[5])
  cart.append(dict(zip(c_keys,c)))

product = []              # product.txt
p_keys = ["cNo","pCode","pName","price","color"]

fff = open("product.txt","r",encoding="utf-8")
while True:
  line = fff.readline()
  if not line: break
  p = line.strip().split(",")
  p[0] = int(p[0])
  p[3] = int(p[3])
  product.append(dict(zip(p_keys,p)))

# 전역변수
chk = 0
cartNo = 0
choice = 0
session_info = {}
#함수구현-------------------------------------------------------------------------------
def buy():
  pass




#--------------------------------------------------------------------------------------
#SM_SHOP 쇼핑몰 구현
while True:
  print("[ SM=SHOP ]")
  print("[ 로그인 화면 ]")
  input_id = input("ID : ")
  input_pw = input("PASSWORD : ")

  for m in member:
    if input_id == m['id'] and input_pw == m['pw']:
      print(f"{m['nickName']}님 환영합니다 !")
      session_info = m
      chk = 1
      break
  if chk == 0:
    print("아이디 또는 비밀번호가 일치하지 않습니다. 다시 로그인하세요.")
  else:
    break

while True:
  print("         [ SM=SHOP ]")
  print(f"                              {session_info['nickName']}님")
  print(f"                     금액 : {session_info['money']:,}원")
  print("")
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈 스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("5. 장바구니")
  print("6. 내용저장")
  print("7. 금액충전")
  print("0. 프로그램 종료")
  choice = input("원하는 상품번호를 입력하세요. >> ")

  if choice == '1':      # 여기서부터 다시 손대시오 !!
    print("삼성TV를 구매하였습니다.")
    print("장바구니에 추가합니다.")
    print()
    now = datetime.datetime.now()
    today = now.strftime("%T-%m-%d %H:%M:%S")
    c = {"cNo":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":session_info['pCode'],"price":session_info['price'],"date":session_info['date'],"date":today}
    session_info['money'] -= product[choice-1]['price']

    cart.append(c)
    cartNo += 1

  elif choice == '2':
    pass
  elif choice == '3':
    pass
  elif choice == '4':
    pass
  elif choice == '5':
    pass
  elif choice == '6':
    pass
  elif choice == '7':
    pass
  elif choice == '0':
    print("프로그램을 종료합니다.")
    break

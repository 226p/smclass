import datetime

member = []
m_keys = ["id","pw","name","nickName","money","address"]

f = open("member.txt","r",encoding="utf-8")    # member.txt
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(",")
  m[4] = int(m[4])     # 금액
  member.append(dict(zip(m_keys,m)))

product = [
  {"pNo":1, "pCode":"t001", "pName":"삼성TV", "price":2000000, "color":"black"},
  {"pNo":2, "pCode":"g001", "pName":"LG냉장고", "price":3000000, "color":"white"},
  {"pNo":3, "pCode":"h001", "pName":"하만카돈 스피커", "price":500000, "color":"brown"},
  {"pNo":4, "pCode":"w001", "pName":"세탁기", "price":1000000, "color":"gray"}
]


cartNo = 0
cart = [
]
c_keys = ["cNo","id","name","pCode","pName","price","date"]

ff = open("cart.txt","r",encoding="utf-8")    # cart.txt
while True:
  line = ff.readline()
  if not line: break
  c = line.strip().split(",")
  c[0] = int(c[0])     # 넘버
  c[5] = int(c[5])     # 금액
  cart.append(dict(zip(c_keys,c)))
ff.close()

session_info = {}
p_title = ["번호","아이디","이름","상품코드","상품명","가격","구매일자"]
chk = 0
#함수---------------------------------------------------------------------
def buy(choice,cartNo):         # 구매 함수
  print(f"{product[choice-1]['pName']}를 구매하였습니다.")
  print("장바구니에 추가합니다.")
  print()
  # 로그인&상품 정보 c
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:%S")
  c = {"cNo":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
  session_info['money'] -= product[choice-1]['price']
  
  cart.append(c)
  cartNo += 1
  return cartNo

def buy_output():              # 장바구니 함수
  print("[ 장바구니 ]")
  print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]:10s}\t{p_title[5]}\t{p_title[6]}")
  print("-"*70)
  sum = 0
  for c in cart:
    sum += c['price']
    print(f"{c['cNo']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:15s}\t{c['price']}\t{c['date']}")
  print(f"총 금액 구매 : {sum:,}")                                        #↑ 10자리수 까지 자리만듬
  print(f"총 구매 건수 : {len(cart)}")

  ff = open("cart.txt","w",encoding="utf-8")
  for c in cart:
    ff.write(f"{c['cNo']},{c['id']},{c['name']},{c['pCode']},{c['pName']:15s},{c['price']},{c['date']}\n")
  ff.close()

def buy_save():                # 내용저장 함수
  f = open("member.txt","w",encoding="utf-8")
  for m in member:
    f.write(f"{m['id']},{m['pw']},{m['name']},{m['nickName']},{m['money']},{m['address']}\n")
  f.close()
  print("내용저장이 완료되었습니다.")

def buy_money():               # 금액충전 함수
  print("[ 금액충전 ]")
  print(f"현재 잔액 : {session_info['money']:,}")
  input_money = int(input("충전할 금액을 입력하세요. >>"))
  session_info['money'] += input_money
  print(f"총 잔액 : {session_info['money']:,}")
#-------------------------------------------------------------------------
while True:
  print("[ 로그인 화면 ]")
  input_id = input("아이디를 입력하세요. >>")
  input_pw = input("비밀번호를 입력하세요. >>")

  # db에서 가져옴
  for m in member:
    if m['id'] == input_id and m['pw'] == input_pw:
      print("SM-SHOP에 오신 것을 환영합니다.")
      session_info = m
      chk =1
      break

  if chk == 0:
    print("아이디 또는 비밀번호가 일치하지 않습니다.")
  else :
    break

while True:
  print("           [ SM-SHOP ]")
  print(f"                                 {session_info['nickName']}님")
  print(f"                     금액 : {session_info['money']:,}원")
  print()
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈 스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("8. 장바구니")
  print("9. 내용저장")
  print("0. 금액충전")
  choice = int(input("원하는 상품번호를 입력하세요. >>"))

  if choice == 1:    # 삼성TV 구매
    cartNo = buy(choice,cartNo)
  elif choice == 2:    # LG냉장고 구매
    cartNo = buy(choice,cartNo)
  elif choice == 3:    # 하만카돈 스피커 구매
    cartNo = buy(choice,cartNo)
  elif choice == 4:    # 세탁기 구매
    cartNo = buy(choice,cartNo)
  elif choice == 8:    # 장바구니 출력
    buy_output()
  elif choice == 9:    # 내용저장
    buy_save()
  elif choice == 0:    # 금액충전
    buy_money()
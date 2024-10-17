import datetime
import os

members = []
m_keys = ["id","pw","name","nickName","address","money"]

f = open('b1017/member.csv','r',encoding='utf-8')    # member.csv
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(",")
  m[5] = int(m[5])
  members.append(dict(zip(m_keys,m)))
f.close()


cartNo = 0
cart = []
c_keys = ["cNo","id","name","pCode","pName","price","date"]

### isdigit 정수인지아닌지 isdir 디렉토리인지 exists 파일존재하는지 isfile 파일인지아닌지
if os.path.exists("b1017/cart.txt"):      # 파일이 없으면 오류라서 있는지 확인부터 ~
  ff = open("b1017/cart.txt","r",encoding="utf-8")    # cart.txt
  while True:
    line = ff.readline()
    if not line: break
    c = line.strip().split(",")
    c[0] = int(c[0])     # 넘버
    c[5] = int(c[5])     # 금액
    cart.append(dict(zip(c_keys,c)))
  ff.close()
else:
  print("파일이 존재하지 않습니다. 파일을 생성해주세요.")

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
print(product)

session_info = {}
chk = 0

#### 함수선언-------------------------------------------------------------------------------
def buy():
  pass
  



#### 프로그램 시작--------------------------------------------------------------------------
## 메인화면
while True:
  print("[ SM_SHOP ]")
  print("[ 메인화면 ]")
  print("1. 로그인")
  print("2. 회원가입")
  print("0. 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요. >>")
  if choice == '1':        # 로그인
    print("[ SM-SHOP ]")
    print("[ 로그인 ]")
    id_input = input("ID: ")
    pw_input = input("PASSWORD: ")
    for m in members:
      if id_input == m['id'] and pw_input == m['pw']:
        print(f"{m['nickName']}님 환영합니다.")
        session_info = m
        chk = 1
        break

    if chk == 0:
      print("ID 또는 PASSWORD가 틀렸습니다. 다시 입력하세요.")
      continue
    else:
      break

  elif choice == '2':
    id = input("ID를 만들어주세요. >>")
    chk = 0
    for m in members:
      if m['id'] == id:
        print(f"{id} : 동일한 아이디가 있습니다. 다시 입력하세요.")
        chk = 1
        break
    if chk == 1:
      continue
    else:
      print(f"{id}는(은) 사용 가능합니다.")
      print()
    pw = input("PW를 입력하세요. >>")
    name = input("이름을 입력하세요. >>")
    nickName = input("닉네임을 입력하세요. >>")
    address = input("주소를 입력하세요. >>")
    money = int(input("충전금액을 입력하세요. >>"))

    m_list = [id,pw,name,nickName,address,money]
    members.append(dict(zip(m_keys,m_list)))

    f = open("member.csv","a",encoding="utf-8")
    for m in members:
      f.write(f"{m['id']},{m['pw']},{m['name']},{m['nickName']},{m['address']},{m['money']}\n")
    f.close()

    print("회원가입을 성공하였습니다. 로그인 해주시길 바랍니다.")
    continue

  elif choice == '0':
    print("프로그램을 종료합니다.")
    break

## 로그인 성공 시 구매화면
while True:
  print("           [ SM-SHOP ]")
  print(f"                         {session_info['nickName']} 님")
  print(f"                     금액 : {session_info['money']} 원")
  print()
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈 스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("8. 장바구니")
  print("9. 내용저장")
  print("0. 금액충전")
  choice = int(input("원하는 상품번호를 입력하세요. >>"))

  if choice == '1':      # 여기서부터 하세유~
    print("삼성TV를 구매하였습니다.")
    print("장바구니에 추가하였습니다.")
    print()
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")

    c = {"cNo":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":product[0]['pCode'],"pName":product[0]['pName'],"price":product[0]['price'],"date":today}
    cart.append(c)
    cartNo += 1
  elif choice == '2':
    pass
  elif choice == '3':
    pass
  elif choice == '4':
    pass
  elif choice == '8':
    pass
  elif choice == '9':
    pass
  elif choice == '0':
    pass





























####-----------------------------------------------------------------------------
  # print("1. 회원등록")
  # print("2. 회원검색")
  # choice = input("원하는 번호를 입력하세요. >>")
  # if choice == '1':
  #   id = input("ID를 만들어주세요. >>")
  #   chk = 0
  #   for m in members:
  #     if m['id'] == id:
  #       print(f"{id} : 동일한 아이디가 있습니다. 다시 입력하세요.")
  #       chk = 1
  #       break
  #   if chk == 1:
  #     continue
  #   else:
  #     print(f"{id}는(은) 사용 가능합니다.")
  #     print()
  #   pw = input("PW를 입력하세요. >>")
  #   name = input("이름을 입력하세요. >>")
  #   nickName = input("닉네임을 입력하세요. >>")
  #   address = input("주소를 입력하세요. >>")
  #   money = int(input("충전금액을 입력하세요. >>"))

  #   m_list = [id,pw,name,nickName,address,money]
  #   members.append(dict(zip(m_keys,m_list)))
  #   print(m_keys)
  #   print("-"*60)
  #   print(members)

  # elif choice == '2':
  #   while True:
  #     m_id = input("아이디를 검색할 단어를 입력하세요.")
  #     mArr = []
  #     for idx,i in enumerate(members):
  #       if i['id'].find(m_id) != -1:
  #         mArr.append(i)
  #         print(i)
  #         chk = 1
  #         break

  #     if chk == 0:
  #       print(f"{m_id}가 들어간 아이디가 없습니다. 다시 입력하세요.")
  #     else:
  #       print(f"{m_id}가 들어간 아이디를 {len(mArr)}개 찾았습니다.")
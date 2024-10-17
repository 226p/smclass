
members = []
m_keys = ["id","pw","name","nickName","address","money"]

f = open('b1017/member.csv','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(",")
  m[5] = int(m[5])
  members.append(dict(zip(m_keys,m)))
f.close()

chk = 0
while True:
  print("1. 회원등록")
  print("2. 회원검색")
  choice = input("원하는 번호를 입력하세요. >>")
  if choice == '1':
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
    print(m_keys)
    print("-"*60)
    print(members)

  elif choice == '2':
    while True:
      m_id = input("아이디를 검색할 단어를 입력하세요.")
      mArr = []
      for idx,i in enumerate(members):
        if i['id'].find(m_id) != -1:
          mArr.append(i)
          print(i)
          chk = 1
          break

      if chk == 0:
        print(f"{m_id}가 들어간 아이디가 없습니다. 다시 입력하세요.")
      else:
        print(f"{m_id}가 들어간 아이디를 {len(mArr)}개 찾았습니다.")
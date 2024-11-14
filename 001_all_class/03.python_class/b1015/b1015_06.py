students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

# 학생성적프로그램에 필요한 전역변수
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0
chk = 0



print("[ 학생성적 삭제 ]")
name = input("찾고자 하는 학생의 이름을 입력해주세요.")
chk = 0
sArr = []
for idx,s in enumerate(students):
  if s['name'] == name:
    choice = input(f"{name} 학생의 정보를 찾았습니다. 학생의 성적을 삭제하겠습니까?\n(삭제 시 복구불가\t1.삭제 0.취소)")
    chk = 1
    if choice == '1':
      del students[idx]
      print(f"{name} 학생의 성적이 정상적으로 삭제되었습니다.")
      sArr.append(s)  # 삭제한 학생의 성적 출력
      break
    else:
      print("학생성적 삭제가 취소되어 이전 화면으로 돌아갑니다.")
      break
  if chk == 0:
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")

# stu_output(s_title,[s])
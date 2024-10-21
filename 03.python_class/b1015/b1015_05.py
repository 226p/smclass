students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"김관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순동","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강홍찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구길","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

def stu_output(s_title,students):    # 학생성적 출력 함수
  print("                     [ 학생성적 출력 ]")
  for title in s_title:
      print(f"{title}\t", end="")  # 상단 타이틀 출력
  print()
  print("-"*60)
  for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()

def stu_search(s_title, students):
  while True:
    chk = 0
    name = input("검색하려는 이름을 입력하세요.(0.취소) >>")
    if name == '0':
      print("학생 성적 검색을 취소하여 이전 화면으로 돌아갑니다.")
      break
    sArr = []
    for idx,s in enumerate(students):
      if s['name'].find(name) != -1:
        sArr.append(s)
        chk = 1

    if chk == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요.")
    else:
      print(f"{name}이 들어가는 학생의 성적을 {len(sArr)}개 찾았습니다.")
      stu_output(s_title,sArr)


stu_search(s_title, students)















# ss = "파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠"
# print(ss.find("자바"))  # find : 없을 시, -1
# print(ss.find("공부"))
# print(ss.index("공부"))  # index : 없으면 error
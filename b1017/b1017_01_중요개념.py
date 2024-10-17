subject = ["국어","영어"]
score = []

while True:
  print("1. 과목추가")
  print("0. 종료")
  choice = input("원하는 번호를 입력하세요. >>")
  if choice == '1':
    s_input = input("과목을 추가하세요. >>")
    subject.append(s_input)
  elif choice == '0':
    break

for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요. >>")))

sum = 0
for i in range(len(subject)):
  print(f"{subject[i]} :",score[i])
  sum += score[i]
print("합계 :",sum)

# num = int(input("국어점수를 입력하세요."))
# num2 = int(input("영어점수를 입력하세요."))
# num3 = int(input("수학점수를 입력하세요."))
# num4 = int(input("과학점수를 입력하세요."))
# num5 = int(input("한국사점수를 입력하세요."))
# print("국어 :",num)
# print("영어 :",num2)
# print("수학 :",num3)
# print("과학 :",num4)
# print("한국사 :",num5)
# print("합계 :",num+num2+num3+num4+num5)




# def output(subject):     # 함수선언
#   print("[과목]")
#   print("-"*20)
#   for s in subject:
#     print(s)

# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요. >>")
#   subject.append(s_input)
#   output(subject)     # 함수호출

# ---------------------------------------------------------------------
# a = 10
# b = 20
# sum = 0

# def add(a,b):     # 함수선언
#   return a+b

# sum = add(a,b)     # 함수호출
# print("a+b 합계 :",sum)

# ---------------------------------------------------------------------
# a = 10     # 전역변수

# def func(a):
#   print("함수 내 a :",a)
#   a += 50
#   return a
#   # global a     # global 전역변수를 가져옴.
#   # a = 50     # 지역변수 - 함수를 종료하면 모두 제거됨.

# a = func(a)
# print("함수 밖 a :",a)

# ---------------------------------------------------------------------

# a = 10     # 전역변수
# b = 20
# c = 30

# def add(a,b,c):
#   return a+b+c     # 함수 내 매개변수는 지역변수로 만들어짐(전역변수와 이름이 같아도 지역변수)

# a = add(a,b,c)
# print(a)
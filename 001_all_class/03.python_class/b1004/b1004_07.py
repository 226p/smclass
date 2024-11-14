# for문 -> 횟수를 정해서 반복할 때
# while문 -> 조건을 정해서 그 조건에 만족하는 동안 반복

# 번호, 이름, 국어, 영어, 수학, 합계, 평균 출력
s_list = []
no = 1
while True:
  name = input("이름을 입력하세요. (종료 : 0) >> ")
  if name == '0':
    break
  kor = int(input("국어점수를 입력하세요. >> "))
  eng = int(input("영어점수를 입력하세요. >> "))
  math = int(input("수학점수를 입력하세요. >> "))
  total = kor + eng + math
  avg = total/3
  
  print(f"번호 : {no}\t이름 : {name}\t국어 : {kor}\t영어 : {eng}\t수학 : {math}\t합계 : {total}\t평균 : {avg:.2f}")
  no += 1

print("프로그램을 종료합니다.")


# 두 수를 입력받아 더하기 뺴기 곱하기 나누기
# while True:
#   num1 = int(input("첫 번째 숫자 입력"))
#   num2 = int(input("두 번째 숫자 입력 (종료 : 0)"))

#   if num2 == 0:
#     break

#   print("[두 수의 사칙연산]")
#   print("*"*30)
#   print("1. 두 수 더하기")
#   print("2. 두 수 빼기")
#   print("3. 두 수 곱하기")
#   print("4. 두 수 나누기")
#   print("*"*30)
#   choice = int(input("원하는 번호를 입력하세요 : "))

#   if choice == 1:
#     print("결과값 : ", num1 + num2)
#   elif choice == 2:
#     print("결과값 : ", num1 - num2)
#   elif choice == 3:
#     print("결과값 : ", num1 * num2)
#   elif choice == 4:
#     print("결과값 : ", num1 / num2)
#   else:
#     print("잘못 입력하셨습니다.")



# 이중while문 
# i=1,10 j=1,10 - j를 1,3,5,7,9 이렇게 출력
# i, j = 1, 1
# print(i, j)

# i, j = 1, 1
# while i<10:
#   while j<10:
#     if j%2 != 0:
#       print(i, j)
#     j += 1
#   j = 1
#   i += 1

# continue 사용
# i, j = 1, 1
# while i < 10:
#   while j < 10:
#     if j % 2 == 0:
#       j += 1
#       continue
#     print(i, j)
#     j += 1
#   j = 1; i += 1



# break - 반복문을 종료 # 근데이거뭔가이상함
# i = 0; j = 0
# while i < 10:
#   print("번호1 : ", i)
#   while j < 10:
#     if j == 5:
#       break # j의 반복문만 종료
#     print("번호2 : ", j)
#     j += 1



# 입력한 숫자를 계속 더하는 프로그램을 만드시오
# 0이 입력되면 프로그램을 종료할 것

# sum = 0
# while True:
#   num = int(input("숫자를 입력하세요 : "))
#   if(num == 0):
#     print("프로그램 종료")
#     break
#   sum += num
#   print("합계 : ",sum)

# 혼자하다 망함
# i_num = 0
# while(i_num>0):
#   i_num = int(input("숫자를 입력하세요 : "))
#   i_num += i_num
#   if(i_num == 0):
#     print("프로그램을 종료합니다.")



# 무한반복
# i = 0
# while True:
#   print(i)
#   i += 1



# i = 0
# while(i < 10):
#   i += 1
#   print(i)

# for i in range(10):
#   print(i)



### 구구단 출력 ###
# while문으로
# i = 1
# while(i<10):
#   j = 1 
#   while(j<10):
#     print(f"{i} x {j} = {i*j}")
#     j += 1
#   i += 1

# for문으로
# for i in range(1,9+1):
#   for j in range(1,9+1):
#     print(f"{i} x {j} = {i*j}")
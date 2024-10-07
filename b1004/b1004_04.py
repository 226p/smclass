### 두 수를 입력받아 두 수까지 합계 구하기 ###
# num1 = int(input("첫 번째 숫자를 입력하시오"))
# num2 = int(input("두 번쨰 숫자를 입력하시오"))

# sum = 0
# for i in range(num1,num2+1):
#   sum += i
# print(f"합계 : {sum}")

# 만약 num1이 num2보다 클 떄
# 1. if문 사용
# num1 = int(input("첫 번째 숫자를 입력하시오"))
# num2 = int(input("두 번쨰 숫자를 입력하시오"))

# min_num = num1
# max_num = num2
# if(num1>num2):
#   min_num = num2; max_num = num1

# sum = 0
# for i in range(min_num,max_num+1):
#   sum += i
# print(f"합계 : {sum}")

# 혼자하다 망한것
# if(num1>num2):
#   for i in range(num1,num2+1):
#     sum += i
# else:
#   for j in range(num2,num1+1):
#     sum += j
# print(f"합계 : {sum}")

# 2. min, max함수 사용
# num1 = int(input("첫 번째 숫자를 입력하시오"))
# num2 = int(input("두 번쨰 숫자를 입력하시오"))
# # min_num = min(num1,num2); max_num = max(num1,num2)

# sum = 0
# for i in range(min(num1,num2),max(num1,num2)+1):
#   sum += i
# print(f"합계 : {sum}")

# # 3. if문 사용2
# num1 = int(input("첫 번째 숫자를 입력하시오"))
# num2 = int(input("두 번쨰 숫자를 입력하시오"))

# if num1 > num2:
#   num1,num2 = num2,num1   # 두 개의 변수 치환 가능. 파이썬만 가능함
# # num1, num2의 값을 치환하고 싶을 때 다른 언어의 경우 이렇게 해야 함
# # num3 = num1 # 일단 텅빈변수를 하나 더 만들어야 함
# # num1 = num2
# # num2 = num3


# sum = 0
# for i in range(num1,num2+1):
#   sum += i
# print(f"합계 : {sum}")



# # 1,3,5,7,9...99 총합
# sum = 0
# for i in range(1,100+1,2):
#   sum += i
# print(f"합계 : {sum}")



# # 1에서 100까지 숫자의 합
# sum = 0
# for i in range(1,100+1):
#   sum += i
# print("합계 : ",sum)



# 0 : 안녕하세요
# 1 : 안녕하세요
# 2 : 안녕하세요
# for i in range(3):
#   print(f"{i} : 안녕하세요")

# for _ in range(3):  # 변수 쓰기 귀찮고 안받아도 되면 _넣어도 됨
#   print("안녕하세요")



# 배열이 1일 때 - 1번 출력,2일때 2번...3일떄 3번...
# for i in [1,2,3]:
#   for j in range(i):
#     print("안녕하세요")
#   print("-"*10)

# for i in [1,2,3]:
#   print("안녕하세요\n"*i,end="")
#   print("-"*10)



# for문을 사용해서
# *****
# **** 
# *** 
# ** 
# * 
# for i in range(5,1-1,-1): # -1씩 감소
#   print("*"*i)



# for문을 사용해서
# * 
# ** 
# *** 
# **** 
# *****  츌력
# for i in range(1,5+1):
#   print("*"*i)

# 망함
# for i in range(1,5+1):
#   for j in range(5):
#     print("*"*j)



# # for i in range(시작값, 끝값+1, 증가값)2 쓰면 2칸씩 띄움 13579
# for i in range(1,10,2): 
#   print(f"[{i}단]")
#   for j in range(1,9+1):
#     print(f"{i} x {j} = {i*j}")



# # 구구단 1,3,5,7,9단만 출력

# for i in range(1,9+1):
#   if(i%2!=0):
#     print(f"[{i}단]")
#     for j in range(1,9+1):
#         print(f"{i} x {j} = {i*j}")



# # 구구단을 출력
# for i in range(2,9+1):
#   print(f"\n[{i}단]")
#   for j in range(1,9+1):
#     print(f"{i} x {j} = {i*j}")
#   print(f"-"*30)



# # 1,3,5,7,9까지 출력
# for i in range(1,10):
#   if(i%2!=0):
#     print(i)



# # 1에서 10까지 for문 사용해서 출력
# for i in range(1,10+1):
#   print(i)
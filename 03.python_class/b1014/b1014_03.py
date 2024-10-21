def plus(n1,n2):
  return n1+n2

n1 = int(input("숫자를 입력하세요."))
n2 = int(input("숫자를 입력하세요."))
print(plus(n1,n2))

#-------------------------------------------------------------------------------
# def plus(n1,n2):
#   result = n1+n2
#   return result

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))

#-------------------------------------------------------------------------------
# def num_sum(st,end):
#   sum = 0
#   for i in range(st,end):
#     sum += i
#   return sum

# print(f"2~50까지 합 : {num_sum(2,50):,d}")    # 1,000 표현
# print(f"3~7까지 합 : {num_sum(3,7):,d}")
# print(f"5~50까지 합 : {num_sum(5,50):,d}")
# total = num_sum(2,50) + num_sum(3,7) + num_sum(5,50)
# print(f"총 합계 : {total:,d}")

#-------------------------------------------------------------------------------
# def num_sum(st,end):
#   sum = 0
#   for i in range(st,end+1):
#     sum += i
#   return sum     # return  호출한 값을 원하는 위치로 되돌려줌

# total = 0
# num_sum(1,10)
# num_sum(1,100)

# total = num_sum(1,10) + num_sum(1,100)
# print("합계 : ",total)

# print("프로그램 종료")

#-------------------------------------------------------------------------------
# def num_sum(st,en):   # (매개변수, 매개변수)
#   sum = 0
#   for i in range(st,en):
#     sum += i
#   print("합계 : ",sum)

# sum = 0
# for i in range(1,11):
#   sum += i
# print("합계 : ",sum)

# num_sum(1,11)
# num_sum(1,101)
# num_sum(2,51)
# num_sum(100,1001)

# num1 = int(input("시작 숫자를 입력하세요."))
# num2 = int(input("끝 숫자를 입력하세요."))

# num_sum(num1,num2+1)
# 함수 - 기본매개변수, 가변매개변수, 키워드 매개변수 
# 1. 기본매개변수 
# def plus(n1,n2):
#   sum = n1+n2
#   print("합계 :",sum)
#   return sum

# plus(10,20)

# 2. 가변매개변수 - 튜플(수정할 수 없는 리스트)타입으로 받음
# def plus(a,*n1):   # 기본매개변수 같이 사용시, 가변매개변수 앞에 사용해야 함
#   print("a :",a)
#   for i in n1:
#     print(i)
#   print(type(n1))

# plus(1,2,3,4,5)

# 3. 키워드 매개변수
# def plus(k=10,m=5):  
#   print("k :",k)
#   print("m :",m)

# plus()
# plus(1,2)
# plus(m=1,k=2)

# print(1,2,3,4,5,sep=" ", end="\t")

# 4. 가변매개변수, 키워드 매개변수 동시 사용할 경우
def plus(*n,k):
  print("k :",k)
  for i in n:
    print(i)

plus(1,2,3,4,5,k=50) # 키워드 매개변수는 무조건 가변매개변수 뒤에 위치

#-----------------------------------------------------------------------
# # 함수선언
# def calc(st,end):
#   for i in range(st,end+1):
#     print(f"[ {i}단 ]")
#     for j in range(1,10):
#       print(f"{i} x {j} = {i*j}")

# calc(2,9)  # 함수호출
# calc(3,7)
# calc(5,9)

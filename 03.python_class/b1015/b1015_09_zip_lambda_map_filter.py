result = 1
for i in range(1,5):
  result *= i  # 재귀함수


# quiz 
a = [1,2,3,4,5]

aArr = list(map(lambda x:x+10,a))  # lambda&map
print(aArr)

bArr = [i+10 for i in a]   # 리스트내포
print(bArr)

# def func(v1,v2):
#   return v1*v2

# lambda v1,v2:v1*v2

# # lambda
# # a = [1,2,3,4]
# # b = [10,20,30,40]
# # #map(lambda 매개변수1, 매개변수2 : 리턴값, 복합자료형1, 복합자료형2)
# # aArr = list(map(lambda i,j:i+j,a,b))
# # print(aArr)

# # 리스트 내포
# a = [1,2,3,4]
# b = [10,20,30,40]
# # # d = []
# # aArr = [i+j for i,j in zip(a,b)]
# # print(aArr)  # 선생님이 구현


# # def num(a,b):   # 내가 구현
# #   for i in range(4):
# #     c = a[i]+b[i]
# #     d.append(c)
# #   print(d)

# aArr = []
# bArr = []
# def func(a,b):  # 선생님이 구현
#   for i,j in zip(a,b):
#     aArr.append(i+j)
#   return aArr
# print(func(a,b))
# # num(a,b)

# def num(a):
#   for i in a:
#     bArr.append(i*i)
#   return bArr
# print(num(a))


# filter(함수,반복가능한 자료형 - 리스트,튜플,딕셔너리)

# zip함수 :2개 리스트 1개로 변경
# a = [1,2,3,4]
# b = [10,20,30,40]
# print(list(zip(a,b)))
# print(dict(zip(a,b)))

# def func(v):
#   if v%2 == 0:
#    return True
#   else:
#     return False

# aArr = [1,2,3,4]     # aArr 값중에 2의 배수인 경우에만 리턴
# bArr = list(filter(func,aArr))
# print(bArr)

# filter&lambda
# aArr = [1,2,3,4]
# bArr = list(filter(lambda x:x%2==0,aArr))
# print(bArr)

# 기본함수사용방법
# def func(v):
#   if v%2 == 0:
#     return v

# aArr = [1,2,3,4]
# bArr = []
# for i in aArr:
#   if func(i) != None:
#     bArr.append(func(i))
# print(bArr)

# def func(v):
#   return v*2

# lambda v:v*2

# # map 함수 - map(함수,리스트) :리스트의 내용을 1개씩 함수에 전달해서 결과값을 리스트로 저장
# # aArr = [1,2,3,4]
# # bArr = list(map(func,aArr))   # map타입이기 때문에 리스트 타입으로 꼭 바꿔사용해야 함
# # print(type(bArr))
# # print(bArr)

# # lambda 
# aArr = [1,2,3,4]
# bArr = list(map(lambda x:x*2,aArr))   # 함수 func 사용 안하고 lambda사용

# 리스트 내포
# aArr = [1,2,3,4]
# print(aArr)
# bArr = [a*2 for a in aArr]
# print(bArr)

# 기본적인 함수사용
# print(func(2))

# aArr = [1,2,3,4]
# print(aArr)

# bArr = []
# for a in aArr:
#   bArr.append(func(a))

# print(bArr)


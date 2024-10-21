a = ((1,2),(3,4),(5,6))
print(a[0])
print(a[0][1])



# 문자열 ---> tuple로 타입 변경
a_str = "abcde"
print(a_str)
print(a_str[1])

a_tu = tuple(a_str)
list(a_tu)
print(list(a_tu))



# <<두수의 치환>>
# a = '우유'
# b = '커피'
# c = ""
# print(a,b)
# # 파이썬 a,b치환
# a,b = b,a
# print(a,b)

# # 기본적인 a,b치환
# c = a
# a = b
# b = c
# print(a,b)

# aArr = [[1,2],[[1,2],[3,4]],[5,6],[7,8]]
# a_list = [1,2,3,4,5,6,7,8]

# b_list = []

# for i in aArr:
#   if type(i) == list:
#     for j in i:
#       if type(j) == list:
#         for k in j:
#           b_list.append(k)
#       else:
#         b_list.append(j)
# print(b_list)


# aArr = [[1,2],[3,4],[5,6],[7,8]]
# a_list = [1,2,3,4,5,6,7,8]

# b_list = []

# for i in aArr:
#   if type(i) == list:
#     for j in i:
#       b_list.append(j)
# print(b_list)


# t = [3,5,1,2]
# t.sort()    # t리스트에 반영
# print(t)    # t 순차배열로 변경

# t[1:3]    # t 변경되지 않음

# print(t+[3,7])   # t 변경되지 않음
# t.extend([3,7])    # t에 반영됨
# print(t)
#---------------------------------------------------------------------------------
# t = (1,2,3,4)     # 튜플 : 리스트와 타입 같음,순서있음 but 수정불가능
# print(t)
# print(t[0])
# # t[0] = 100     # 튜플 수정, 추가불가  읽기만 가능
# print(len(t))

# t = t+(3,5)     # 더하기 연산자로 추가 가능
# print(t)

# tt = (1,2,3)     # 곱하기 연산자 사용 가능 tt에 넣어야 함 
# tt = tt * 2
# print(tt)

# for i in t:    # for문 가능
#   print(i)

# tArr = [1,2,3,4]
# tArr[0] = 100
# print(tArr)
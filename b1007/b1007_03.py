# # 2차원 리스트
# a_list = [
#  [1,2],
#  [5,6,7,8],
#  [9,11,12]
# ]

# # 2차원 리스트 --> for문을 2번 사용
# for i in a_list:
#   for j in i:
#     print(j)


# a_list = []    # 0항, 1항, 2항, 3항 ... 8항
# for i in range(9):
#   a_list.append(i+1)
# print(a_list)

# b_list = []
# for i in range(1,10):
#   b = []
#   if(a_list[i]%4)==0:      # 1,2,3  4,5,6  7,8,9
#     b.append(a_list[i])

# a_list = []
# for i in range(5):
#   a = []
#   a_list.append(a)
#   for j in range(5):
#     a.append(5*i + (j+1))
# print(a_list)


a_list = []
for i in range(5):
  a = []
  a_list.append(a)
  for j in range(5):
    a.append(5*i+(j+1))
print(a_list)


# ★ 아래 구조 외우기 ★ 1~9까지 리스트 추가(2차원 리스트)
# a_list = []
# for j in range(0,3):
#   a = []
#   a_list.append(a)
#   for k in range(0,3):
#     y = 3*j + (k+1)     # 3x+y
#     a.append(y)      
# print(a_list)

# 1~9까지 리스트 추가(1차원 리스트)
# b_list = []
# for i in range(1,10):
#   b_list.append(i)
# print(b_list)
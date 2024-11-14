# 1차원 리스트 - 25개
a_list = []
for i in range(25):
  a_list.append(i)
print(a_list)

# 1차원 리스트 --> 2차원 리스트 변경
# (0,25,5씩 증가)
b_list = []
for u in range(0,len(a_list),5):
  b_list.append(a_list[i:i+5])    #0:5 , 5:10 , 10:15 ...
print(b_list)


# 1차원 리스트 --> 2차원 리스트 변경
# b_list = []
# for i in range(5):
#   a = []
#   b_list.append(a)
#   for j in range(5):
#     a.append(5*i+(j+1))
# print(b_list)


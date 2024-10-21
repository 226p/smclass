import random

a_list = []

for i in range(25):
  a_list.append(i+1)
random.shuffle(a_list)
print(a_list)


#0~25까지 5씩 증가 (0,25,5)
# b_list = []
# for i in range(0,len(a_list),5):
#   b_list.append(a_list[i:i+5])
# print(b_list)

# b_list 랜덤으로 섞어서 1~25까지 [5,5] 2차원 리스트   ↓x축, →y축
# while True:
#   print("\t0\t1\t2\t3\t4")
#   print("-"*60)
#   for i in range(5):
#     print(i,end='\t')
#     for j in range(5):
#       print(b_list[i][j],end='\t')
#     print()
#   input1 = input("좌표를 입력하세요.[x,y]>> ")
#   input2 = input1.split(",")
#   print(input2)
#   print(f"{input1}의 좌표 값 : ",b_list[int(input2[0])][int(input2[1])])



# while len(a_list)<25:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)

# b_list = []
# for i in range(5):
#   a = []
#   for j in range(5):
#     a.append(a_list[5*i+j])     # a_list[0], a_list[1], a_list[2], a_list[3], a_list[4]
#   b_list.append(a)
# print(b_list)



# for j in range(5):
#   b = []
#   for k in range(5):
#     b.append(5*j + (k+1))
#   b_list.append(b)

# print(b_list)
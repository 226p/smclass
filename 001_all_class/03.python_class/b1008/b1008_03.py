# [5,5] 2차원리스트
import random

aArr = []
for i in range(25):
  aArr.append(i+1)
random.shuffle(aArr)
# print(aArr)

a_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append(aArr[5*i+j])
  a_list.append(a)

while True:
  print("\t0\t1\t2\t3\t4")
  print("-"*50)
  for i in range(5):
    print(i,"|",end='\t')
    for j in range(5):
      print(a_list[i][j],end='\t')
    print()

  # 값 입력 --> 좌표 출력
  aa = int(input("값을 입력하세요.(1~25) >>"))
  if 0 > aa or aa > 26:
    print("1~25사이의 값을 입력해야 합니다.")
    continue
  for i in range(5):
    for j in range(5):
      if a_list[i][j] == aa:
        print(f"좌표값 : {i,j}")
        a_list[i][j] = "-"
        break



  # 좌표 입력 --> 해당 값 출력
  # re = input("좌표를 입력하세요.(x.y) >>")
  # result = re.split(".")
  # print("좌표값 :",a_list[int(result[0])][int(result[1])])


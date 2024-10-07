import random

lotto = [0]*6 + [1]*3
random.shuffle(lotto)
a_list = []

for i in range(3):
  a = []
  for j in range(3):
    a.append(lotto[3*i+j])
  a_list.append(a)
# print(a_list)

aa_list = [
  ["로또","로또","로또"],
  ["로또","로또","로또"],
  ["로또","로또","로또"]
]

while True:
  my_money = int(input("얼마를 투자하겠습니까?"))

  print("        [i,j 좌표]")
  print("\t0\t1\t2")        # y축 꾸미기
  print("-"*30)
  for i in range(3):
    print(i,"|",end='\t')
    for j in range(3):
      print(aa_list[i][j],end='\t')
    print()

  code = input("좌표를 입력하세요.(x,y) >>")
  codeArr = code.split(".")

  if a_list[int(codeArr[0])][int(codeArr[1])] == 1:
    aa_list[int(codeArr[0])][int(codeArr[1])] = "당첨~"
    print(f"당첨~ 당첨금 : {my_money*10:,d}원")   # :,d 1000단위로 , 넣음

  else:
    aa_list[int(codeArr[0])][int(codeArr[1])] = "꽝!"
    print("꽝! 다음 기회에....")
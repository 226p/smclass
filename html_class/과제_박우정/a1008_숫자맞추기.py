# 숫자맞추기 게임 과제  1~100 맞추기, 자신이 입력한 숫자를 저장해서 출력
import random

r_num = random.randint(1,100)
count = 0
for i in range(10):
  input_num = int(input("1~100까지 숫자를 입력하세요. 기회는 단 10번!! >>"))
  if input_num < r_num:
    print("입력한 숫자가 정답보다 작습니다. 더 큰 숫자를 적어주세요.")
    print()
  elif input_num > r_num:
    print("입력한 숫자가 정답보다 큽니다. 더 작은 숫자를 적어주세요.")
    print()
  else:
    print(f"정답입니다. 정답 : {r_num}")
    count = 1
    break

if count == 0:
  print("10번 도전 실패!!")

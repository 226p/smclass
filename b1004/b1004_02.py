import random



# 10번 도전해서 입력한 숫자가 더 크면 작은 수를 입력하셔야 합니다.
# 10번 도전해서 입력한 숫자가 더 작으면 큰 수를 입력하셔야 합니다.
# 10번 도전해서 맞히지 못하면  10번 도전에 실패했습니다. 정답 : ㅁㅁㅁ
# 10번 도전 성공시 > 도전에 성공했습니다. 정답 :

i = 0
count = 0
r_num = random.randint(1, 100)
while i < 10:
  i_num = int(input(f"{(i+1)}번째 숫자를 입력하세요 : "))
  if(i_num > r_num):
    print("입력한 숫자가 큽니다.")
  elif(i_num < r_num):
    print("입력한 숫자가 작습니다.")
  else:
    print(f"도전 성공! 정답 : {i_num}")
    count = 1
    break
  i += 1
if count == 0:
  print(f"10번 도전에 실패했습니다. 정답 : {r_num}")
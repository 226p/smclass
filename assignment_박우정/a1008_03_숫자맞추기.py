# 1~100 숫자맞추기 게임 / 입력한 숫자들은 리스트에 저장해서 함께 출력할 것
import random

r_num = random.randint(1,100)
count = 0
i = 0
num_list = []

for i in range(10):
    print("1~100까지의 숫자를 입력하세요. 단, 기회는 10번!!")
    input_num = int(input(f"{i+1}번째 숫자를 입력하세요 : "))
    print()
    if r_num > input_num:
        print("입력한 숫자가 작습니다. 더 큰 숫자를 입력해주세요.")
        print()
    elif r_num < input_num:
        print("입력한 숫자가 큽니다. 더 작은 숫자를 입력해주세요.")
        print()
    else:
        print(f"도전 성공!! 정답 : {r_num}")
        count = 1
        break
    n = input_num
    num_list.append(n)
    print(num_list)
    i += 1

if count == 0:
    print(f"10번 도전에 실패했습니다. 정답 :{r_num}")
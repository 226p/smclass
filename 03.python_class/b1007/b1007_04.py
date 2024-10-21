import random

# num = int(random.random()*25)+1    # 1,25의 랜덤숫자 생성


a_list = []
# 1~25 랜덤숫자 입력하는데, 중복제거하고 출력

# for i in range(25):
#   num = random.randint(1,25)     # 1,25의 랜덤숫자 생성
#   if num not in a_list:
#     a_list.append(num)
# print(a_list)

# while len(a_list)<25:        # 25보다 숫자가 적으면 채워넣기
#   num = random.randint(1,25)     # 1,25의 랜덤숫자 생성
#   if num not in a_list:          # a_list안에 중복숫자 제거
#     a_list.append(num)
# print(a_list)

# 1~25까지 랜덤으로 패치   random.sample()
a_list = []
for i in range(25):
  a_list.append(i+1)
# b_list = random.sample(a_list,25)    # 범위 리스트, 25개 추출(중복추출 안됨)
# print(b_list)


# 1~25까지 랜덤으로 패치   random.choices()
b_list = random.choices(a_list,k=25)      # 범위 리스트, 중복가능한 25개 추출
print(b_list)
# for문 출력
for k in range(1,9+1):
  print(f"[ {k}단 ]",end="\t\t")
print()
for i in range(2,9+1):
  for j in range(1,9+1):
    print(f"{j} x {i} = {j*i}", end="\t")
  print()




# 000
# 001
# ...
# 999

### for 1개 사용 ###
# a = 1
# for i in range(1000):
#   print(f"{i:03d}")

### for 3개 사용 ###
# for i in range(0,9+1):
#   for j in range(0,9+1):
#     for k in range(0,9+1):
#       print(f"{i}{j}{k}")



# # 구구단 - 입력받은 숫자 단까지 출력. 3 입력 -> 123단, 5단 입력 -> 12345단
# dan = int(input("1부터 9까지 숫자를 입력하시오"))
# # if(0>dan>10):
# #   print("숫자를 잘못 입력하셨습니다. 1부터 9까지 입력하세요")

# for i in range(dan,dan+1):
#   print(f"[{i}단]")
#   for j in range(1,9+1):
#     print(f"{i} x {j} = {i*j}")
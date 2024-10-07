# # 0부터 1씩 증가하면서 10번 실행 (0-9)
# for i in range(10):
#   print(i)

# # 5부터 10 이전까지 실행
# print("-"*10)
# for j in range(5,10):
#   print(j)

# print("-"*10)
# a_list = [1,2,3,4,5]
# for k in a_list:
#   print(k)


# 파이썬 - 문자열(str), 정수형(int), 실수형(float), 논리형(bool)

# <배열 종류>
# 리스트 타입 - []
# 딕셔너리 타입 - {} : json타입과 모양이 같음. 키, 값(key, value)
dic = {
  "번호":1,
  "이름":"ㅇㅇㅇ",
  "국어":100,
  "영어":100,
  "수학":100
}
print(dic["번호"])
print(dic["이름"])

for n in dic:   # dic에서 key값을 n에 넣어줌
  # print(n)    # key값이 출력됨
  print(dic[n]) # value값이 출력됨

# print("-"*10)
# b_list = [1,3,9,10,20]
# for m in b_list:
#   print(m)

# # 리스트 길이 : len()
# print("-"*10)
# print(len(b_list))

# # 리스트 안에 중복되는 숫자가 몇 개인지 확인하는 것
# print("-"*10)
# b_list = [1,3,9,10,20,3,3,10,5,20]  
# print(b_list.count(3))

# # 리스트에 추가 - append, insert, extend([2,3] - 리스트 추가)
# # 리스트에 삭제 - del, remove, clear(모두삭제)

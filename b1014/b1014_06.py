import random

# fName = ["바나나","오렌지","체리","파인애플","코코넛"]
fruit = {"바나나":"banana","오렌지":"orange","체리":"cherry",
         "파인애플":"pineapple","코코넛":"coconut"}
fName = list(fruit.keys())

print(fName)


# print("[ 랜덤 영어단어 맞추기 ]")
# re_fName = random.sample(fName,5)
# for i in re_fName:
#   search = input(f"{i}의 영문을 입력하세요.")
#   if fruit[i] == search:
#     print("정답 :",search,fruit[i])
#   else:
#     print("오답 :",search,fruit[i])

# print("[ 순서대로 영어단어 맞추기 ]")
# for key in fruit.keys():
#   search = input(f"{key}의 영문을 입력하세요.")
#   if fruit[key] == search:
#     print("정답 :",search,fruit[key])
#   else:
#     print("오답 :",search,fruit[key])

# print(fruit["바나나"])

# while True:
#   search = input("과일이름을 입력하세요. >> ")
#   if search in fruit:
#     print("영문으로 :", fruit[search])
#   else:
#     print("찾는 단어가 없습니다. 다시 입력하세요.")

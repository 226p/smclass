ss = "파이썬 수업중 타입 문자열 타입, 정수형 타입, 실수형 타입, 논리형 타입이 있습니다."
i_str = input("검색할 단어를 입력하세요.")

# sss = ss.replace("타입","atype") 글자바꾸기 (공백제거로 활용도 함 "","")
# print(sss)

# a_str = "파이썬"
# a = "-".join(a_str)
# print(a)

# 타입의 위치값 모두 출력(★)  ----> 집가서 꼭 다시하슈
a_list = []
idx = 0
for s in range(ss.count(i_str)):
  num = ss.find((i_str),idx)   # 0번부터 시작 - 8,15,23,31,39
  a_list.append(num)
  idx = num+1

print(f" 검색개수 : {len(a_list)}, 위치값 : {a_list}")



# 검색 글자 개수
# idx = ss.count(i_str)
# print("위치값 :",idx)

# 글자 유무 확인
# idx = ss.find(i_str)
# print("위치값 :",idx)

# idx = ss.find("타입")+1
# print(ss.find("타입", idx))     # find값은 하나만 찾아줘서 새로운 기준점 명시 ,9 (8위치에 있기 때문에 +1(9)부터 찾는 글자 위치 확인)



# idx = ss.index(i_str)
# print("위치값 :",idx)  ---> 글자가 없으면 error 프로그램 꺼지니까 find쓰는게 나음


# if i_str in ss:
#   print("있습니다.")
# else:
#   print("없습니다.")

# aArr= [1,2,3,4,5]
# a_list = [i*i for i in aArr]
# print(a_list)

# a_list = []
# for i in range(1,21):
#   if i%3 == 0:
#     a_list.append(i)
# print(a_list)


# b_list = [i for i in range(1,21) if i%3 == 0]   # 리스트 내포 [값 for문 조건식]
# print(b_list)
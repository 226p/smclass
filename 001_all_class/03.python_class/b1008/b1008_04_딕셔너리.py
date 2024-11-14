dic1 = {"번호":1,"이름":"홍길동", "kor":100, "eng":100}
dic1["math"] = 90      # 딕셔너리 추가 : 없는 키와 값을 입력하면 추가
dic1["kor"] = 50       # 딕셔너리 변경 : 있는 키에 값을 입력하면 수정
del(dic1['eng'])       # 딕셔너리 삭제 : del(키) 입력하면 삭제
print(dic1)             # 딕셔너리 전체 출력
print(dic1["이름"])       # 출력 방법 : key 입력하면 값을 출력
# print(dic1["합계"])                  # 없는 키를 입력하면 error
print(dic1.get("이름"))   # 출력 방법2
print(dic1.get("학번"))   # 없는 키를 입력하면 error는 안나지만 None 나옴
for key in dic1.keys():   # 모든 키 출력
  print(key, dic1[key])

if dic1.get("이름") != None:
  print(dic1.get("이름"))

print(type(dic1.keys()))        # type : 딕셔너리 타입은 class객체 (index값 없음)
print(dic1.keys())        # 모든 키 값 출력
print(list(dic1.keys()))       # 타입 변경 class -> list

print(list(dic1.keys())[0])

print(dic1.values())          # 값 출력(class객체)
print(list(dic1.values()))      # 타입 변경 class -> list

print(dic1.items())               # 튜플 타입(리스트와 같지만 수정이 불가능)
print(list(dic1.items()))

for key in dic1:            # 키만 추출
  print(key)

for key in dic1:          # 값만 추출
  print(dic1[key])

for key, val in dic1.items():       # 키,값 추출
  print(key, val)

# 평균이 없을 때만 평균을 추가
if "평균" not in dic1:
  dic1["평균"] = 99.0


a_list = [1, "홍길동", 100, 100, 100, 300, 100, 0, 1] # 리스트 값의 의미를 알 수 없지만 딕셔너리는 key 덕분에 의미를 알 수 있음


# a_list = [1,2,3,"홍길동"] 
# print(a_list[0])  # 값이 없기 때문에 주소값으로 출력했었음
# # append, insert, extand    리스트 추가
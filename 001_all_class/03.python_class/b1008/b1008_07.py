import operator

#zip()함수
# name = ["홍길동","유관순","이순신"]
# score = [100,90,95]


# d_dic = dict(zip(name,score))   # 딕셔너리 타입 리스트 생성
# print(d_dic)

# n_list = list(zip(name,score))  # 튜플 타입 리스트 생성
# print(n_list)


# n_list = []
# for n,s in zip(name,score):   # 동시에 여러개 리스트에 접근
#   n_list.append([n,s])
#   print(n,":",s)
# print(n_list)

#-----------------------------------------------------------------------------------
# <<for문 1줄로 처리 (리스트내포, 컴프리헨션)>>
# nList = [i+1 for i in range(5)]
# print(nList)

# a_list = [i*i for i in range(5)]
# print(a_list)

# # 정수형 ---> 문자형
# b_list = [str(i) for i in range(5)]
# print(b_list)

# # 문자형 ---> 정수형
# c_list = ["5","9","0","3","2"]
# cc_list = [int(i) for i in c_list]
# print(cc_list)

# d_str = "1,2,23,5,9"
# d_sp = [int(i) for i in d_str.split(",")]
# print(d_sp)

# # 문자열을 입력받아 정수형 리스트로 변경
# score = input("좌표를 입력하세요.(0,0) >>")
# sc = [int(i) for i in score.split(",")]
# print(score)
# print(sc)
#-----------------------------------------------------------------------------------

# students = [
#   {"no":1, "name":"홍길동", "kor":100, "eng":100, "math":99, "total":299, "avg":99.67, "rank":0},
#   {"no":2, "name":"유관순", "kor":80, "eng":80, "math":85, "total":245, "avg":81.67, "rank":0},
#   {"no":3, "name":"이순신", "kor":90, "eng":90, "math":91, "total":271, "avg":90.33, "rank":0},
#   {"no":4, "name":"강감찬", "kor":60, "eng":65, "math":67, "total":192, "avg":64.00, "rank":0},
#   {"no":5, "name":"김구", "kor":100, "eng":100, "math":84, "total":284, "avg":94.67, "rank":0},
# ]

# for s in students:
#   print(s)
# x = sorted(students)
# print("-"*50)
# print(students)





#-----------------------------------------------------------------------------------
# <<딕셔너리에 대한 정렬>>

# nameDic = {'홍길동':100, '유관순':80, '이순신':95, '강감찬':82, '김구':97}

# key, value - nameDic.items()
# key - nameDic.keys()
# value - nameDic.values()
# key - [0], value - [1]
# (key,value) : [0,1]
# nameDics = sorted(nameDic.items(),key=operator.itemgetter(1))         # [1]번째 이름 순차정렬(value로 정렬)

# nameDics = sorted(nameDic.items(),key=operator.itemgetter(1),reverse=True)   # [1]번째 이름 역순정렬(value로 정렬)

# nameDics = sorted(nameDic.items(),key=lambda x:x[0])    # 람다식으로 [0]번째 순차정렬
# nameDics = sorted(nameDic.items())    # [0]번째 이름 순차정렬(key로 정렬)
# nameDics = sorted(nameDic.items(),reverse=True)    #[0]번째 이름 역순정렬(key로 정렬)
# print("-"*50)
# print(nameDics)
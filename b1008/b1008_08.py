import copy

name = ["홍길동","유관순","이순신"]
score = [100,90,95]

n_dic = dict(zip(name,score))
print(n_dic)

a = copy.deepcopy(n_dic)                  # 딕셔너리의 깊은 복사
a['홍길동'] = 0
print(a)
print(n_dic)


# a = n_dic                    # 딕셔너리의 얕은 복사

#--------------------------------------------------------------------------------

# 얕은 복사
# name = ["홍길동","유관순","이순신"]

# # n = name  # name의 값을 n에 복사
# # n[2] = "김구"
# # print(n)   # n의 이순신 -> 김구 변경
# # print(name)   # n의 이순신 -> 김구 변경


# # 깊은 복사
# n = name[:]
# n[2] = "김구"
# print(n)
# print(name)
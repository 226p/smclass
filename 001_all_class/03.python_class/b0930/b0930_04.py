a = input("이름을 적으시오.")
b = input("국어 점수를 적으시오.")
c = input("영어 점수를 적으시오.")
d = input("수학 점수를 적으시오.")

# print(type(b))
total = int(b)+int(c)+int(d)  # 문자열에서 정수형으로 타입 변경

print("{}, {}, {}, {}, {}, {:.2f}".format(a, b, c, d, total, (total)/3))




# a = '100'
# print(type(a))

# b = "200"
# print(type(b))

# name = "홍길동"
# print(a+b)    # 문자 연결 연산자로 나옴
# print(int(a)+int(b))  # 타입변경(문자 -> 숫자) but 텍스트는 불가능
# c = "3.14"
# d = 3.14
# print(int(float(c)))  # 실수로 변경 후 정수형으로 변경 가능 but 바로 문자실수를 바로 정수로 변경 불가능

# print(str(d))   # 실수를 문자로 변경

# e = "True"
# print(bool(e))    # 문자불형은 불형으로 변경

# # var1 = 100
# # var2 = var1
# # var3 = var2
# # var4 = var3

# print(var4)

# v4 = v3 =  v2 = v = 10
# print(v4)

# name = "홍길동"
# print(type(name))

# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True    # 대문자로 넣어야함
# print(type(a_bool))
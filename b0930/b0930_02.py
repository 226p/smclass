
# 10은 2의 배수입니다.
print("%d은 %d의 배수입니다." % (10,2))
a = 10
b = 2
# print 1, 쉼표, %, .format, f
# print(a,"은",b,"의 배수입니다.")
# print("%d은 %d의 배수입니다." % (a,b))
# print("{}은 {}의 배수입니다.".format(a,b))
# print(f"{a}은 {b}의 배수입니다.")

# print("%d * %d = %d" % (a,b,a*b))  

# # 사용 표시
# name = "홍길동"
# kor = 100
# eng = 100
# math = 99

# print("%s 총합 : %d, 평균 : %.2f" % (name, kor+eng+math, (kor+eng+math)/3))

# 자리수 표시
# print("%d" % b)
# print("%5d" % b) #공간 5자리 확보(스페이스바 5번)
# print("%05d" % b) #공간 5자리 확보(0으로 채움)

# num = 1
# num2 = 10
# num3 = 100
# print("%03d" % num)
# print("%03d" % num2)
# print("%.2f" % num3)
# print("%03d %03d %.2f" % (num,num2,num3))

# print("%5d" % (-10))

num = 758.12345678
num3 = 150.15

print("%.2f" % num)

print("%013.2f" % (25.05))

print("%d" % num3)
print("%f" % num3)
print("%s" % num3)

print("*"*10)
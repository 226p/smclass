


def calc():
  global sum     # 전역변수인 경우, 함수에서 변경 시 외부에서도 같이 변경됨
  sum = 200
sum = 10
calc()           # 함수에서 sum을 200으로 변경
print(sum)

# 매개변수가 일반변수(문자열,정수열,실수열,논리열)일 경우, return 하지 않으면 변수값이 변동없음
hh = 100

def add(hh):
  hh = hh +100
  return hh

hh = add(hh)
print(hh)

#-----------------------------------------------------------------------------------
# 복합변수를 매개변수로 전달이 되면, return 없어도 값이 변경되어 전달됨
hong = [1,2,3,4,5]     # 복합(매개)변수(튜플, 딕셔너리)
# kim = []

def add(h):
  for i in range(len(h)):
    h[i] = h[i]+100 

add(hong)
print(hong)

# kim = hong
# kim[0] = 100     # 얕은복사

# print(kim)
# print(hong)

#------------------------------------------------------------------------------------졸아서 다시보셈
# def calc(n1,n2):
#   s1 = n1+n2
#   s2 = n1-n2
#   s3 = n1*n2
#   s4 = n1/n2
#   s5 = [s1,s2,s3,s4]
#   return s5

# s5 = calc(10,5)
# # print(s1)
# # print(s2)
# # print(s3,s4)
# print(s5)
# print("프로그램 종료")

# 함수 내에 선언된 변수를 외부에서 사용할 수 없음
# def calc(v1,v2):
#   global sum                  # 전역변수
#   # sum = 0                   # 지역변수
#   for i in range(v1,v2+1):
#     sum += i
#   return sum

# sum = 100
# sum = calc()


#------------------------------------------------------------------------------------
# sum = 0
# print(0)
# print(1,2,sep=":",end="\t")  # 가변매개변수

# def calc(n1 = 10,n2 = 20):   # 키워드매개변수 : 매개변수의 값이 없을 시 값을 지정해줌
#   print(n1)
#   print(n2)
# calc()
# calc(300)
# calc(n2=200)


# def calc(*n):    # * 가변매개변수 : 갯수 상관없이 리스트타입(튜플) 출력
#   print(n)
#   print(len(n))
# calc(1,2,3)

#------------------------------------------------------------------------------------
# 매개변수를 배열로 변환하여 사칙연산
# def calc(numStr2):
#   s1 = 0
#   s2 = 0
#   s3 = 1    # 곱, 나누기는 0이면 0이라서 1로 해야함
#   s4 = 1
#   for i in range(len(numStr2)):
#     s1 += numStr2[i]
#     s2 -= numStr2[i]
#     s3 *= numStr2[i]
#     s4 /= numStr2[i]
#   print(f"두 수의 합 : {s1}")
#   print(f"두 수의 차 : {s2}")
#   print(f"두 수의 곱 : {s3}")

# numStr = input("숫자를 입력하세요. (12,5,3)>>")
# numStr2 = numStr.split(",")
# numStr2 = [int(i) for i in numStr2]          # 리스트 내포

# calc(numStr2)

#------------------------------------------------------------------------------------
# 세 수를 입력받아 사칙연산
# numStr = input("숫자를 입력하세요. (12,5,3)>>")
# numStr2 = numStr.split(",")
# num = int(numStr2[0])
# num2 = int(numStr2[1])
# num3 = int(numStr2[2])

# def calc(num,num2,num3):
#   print(f"세 수의 합 : {num+num2+num3}")
#   print(f"세 수의 차 : {num-num2-num3}")
#   print(f"세 수의 곱 : {num*num2*num3}")

# calc(num,num2,num3)

#------------------------------------------------------------------------------------
# 입력받은 두 수를 함수로 활용한 사칙연산
# num = int(input("숫자를 입력하세요."))
# num2 = int(input("숫자를 입력하세요."))

# def calc(num,num2):
#   print(f"두 수의 합 : {num+num2}")
#   print(f"두 수의 차 : {num-num2}")
#   print(f"두 수의 곱 : {num*num2}")
#   print(f"두 수의 나누기 : {num/num2}")

# calc(num,num2)

#------------------------------------------------------------------------------------
# 함수를 활용한 사칙연산
# def calc(num,num2):
#   print(f"두 수의 합 : {num+num2}")
#   print(f"두 수의 차 : {num-num2}")
#   print(f"두 수의 곱 : {num*num2}")
#   print(f"두 수의 나누기 : {num/num2}")

# num = [10,20,30]
# num2 = [5,7,3]

# for i in range(3):
#   calc(num[i],num2[i])

#------------------------------------------------------------------------------------
# # for문 활용한 사칙연산
# num = [10,20,30]
# num2 = [5,7,3]

# for i in range(3):
#   print(f"두 수의 합 : {num[i]+num2[i]}")
#   print(f"두 수의 차 : {num[i]-num2[i]}")
#   print(f"두 수의 곱 : {num[i]*num2[i]}")
#   print(f"두 수의 나누기 : {num[i]/num2[i]}")

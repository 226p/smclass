##### 원의 넓이
# r = float(input("원의 반지름을 입력하세요."))
# a = ((r)**2)*3.14
# print("원의 넓이 : {:.2f}".format(a))

#####삼각형의 넓이, 직사각형의 넓이 
# n = input("2개의 길이를 입력하세요")
# print(n.split(" ")) -> 두개의 값 분리

# n_list = n.split(" ")
# n2 = float(input("높이를 입력하세요"))
# b = float(n_list[0])*float(n_list[1])*0.5
# c = float(n_list[1])*n2
# print("삼각형의 넓이 : {}, 직사각형의 넓이 : {}".format(b,c))

stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [1,"유관순", 100,100,100,99],[2,"이순신", 100,99,98,99],[3,"김구", 80,100,90,99]

print("                    [학생 성적 프로그램]")
for s_t in stu_title:
  print("{}".format(s_t),end='\t')   # end 끝을 빈공간 여백을 주고 한 줄로 쓰기(안쓰면 줄단락 \n이랑 같음)
print()       # 다 붙으니까 한번 줄단락 바뀌게 print만듦
print("-"*60)
for s in stu_datas[0]:    # 배열 하나하나 데이터 출력
  print("{}".format(s),end='\t')
print()   
for s in stu_datas[1]:   
  print("{}".format(s),end='\t')
print()   
for s in stu_datas[2]:    
  print("{}".format(s),end='\t')


# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],stu_title[4],stu_title[5],stu_title[6],stu_title[7],))




# a = stu_datas[1][1]
# b = stu_datas[1][2]
# c = stu_datas[1][3]
# d = stu_datas[1][4]

# print("이순신의 평균 : {}".format((a+b+c+d)/4))

# stu_data = ["홍길동", 100,100,100,99]
# a = stu_data[0]
# b = stu_data[1]
# c = stu_data[2]
# d = stu_data[3]
# e = stu_data[4]
# print("학생이름 : {}".format(a))
# print("국어점수 : {}".format(b))
# print("영어점수 : {}".format(c))
# print("수학점수 : {}".format(d))
# print("과학점수 : {}".format(e))
# print("합계 : {}".format(b+c+d+e))
# print("평균 : {}".format((b+c+d+e)/4))


#####복합대입연산자
# a=10
# a+=5; print(a)
# a-=5; print(a)
# a*=5; print(a)
# a/=5; print(a)
# a//=5; print(a)
# a**=5; print(a)
# a%=5; print(a)

##### 사측연산
# a = 5; b=3 # 한 줄로 적을 때 ;붙여주면 됨
# print("{}, {}, {}, {}".format(a/b, a%b, a//b, a**b))

##### 우선순위
# print((2 + 2) - (((2 * 2) / 2) * 2))   # *,/우선순위이기 때문에 괄호 넣어주면 좋음

# a=100
# b=10
# print(str(a)+str(b))  # 다른형태끼리 + 불가능

# 1,2,3....10 -> 1
# 11,12,13.....20 -> 11
# 21,22,23.....30 -> 21   숙제 
# a = input("숫자를 입력하세요")
# print()

##### 여러 줄을 1줄로 선언
# a=10;b=5  #1줄 선언
# s1,s2,s3 = 1,2,3  #1줄 선언

# c = "100"
# d = "10.5"
# print(float(c))  # 정수형 -> 정수, 실수형 가능 but 실수형 -> 실수형만 가능
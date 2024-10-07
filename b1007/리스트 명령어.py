# 리스트 함수
a_list = [1,2,3,4,5,60,3,3,70,3]
# print(len(a_list))   # 리스트 개수
# print(a_list.count(3))   # 입력된 값의 존재 개수
a_list.pop(2)       # 해당 index 위치 삭제
print(a_list)

# a_list.insert(0,100)    # index위치에 해당값 저장
# a_list.append(200)       # 마지막에 값 추가
# a_list.remove(5)       # 입력된 값 찾아 리스트 삭제(5번째가 아니라 5라는 값)
# a_list.clear()        # 전체삭제

# 리스트 삭제(명령어)
# a_list = [1,2,3,4,5,6,7]
# a_list = []      # 전체 삭제(더 많이 씀)
# del(a_list[3])     # 해당 위치 리스트 삭제
# del(a_list)     # a_list 자체를 삭제
# a_list = None  # 전체 삭제
# a_list[1:3] = []  # 2개 삭제
# print(a_list)

# del 명령어 사용
# del a_list[0]   # 0번째 리스트(1) 삭제


# 리스트 수정방법
# a_list = [1,2,3,4,5,6,7]
# a_list[3] = 50   # 4 -> 50   1개 변경시
# a_list[1:2] = [20,30]   # 2 -> 20, 3 -> 30  2개 변경시
# a_list[4] = [10,20]    # 리스트 안에 리스트로 변경(2차원 리스트)
# print(a_list)



# a_list = [1,2,3,4,5]
# b_list = [50,100]

# # 리스트 출력방법
# print(a_list[0:3])  # [1,2,3]
# print(a_list[:3])  # [1,2,3]
# print(a_list[3:])  # [4,5]
# print(a_list[2:4])  # [3,4]
# print(a_list+b_list)  # [1,2,3,4,5,50,100]
# print(b_list * 3)   # [50,100,50,100,50,100]
# print(a_list[::2])   # [1,3,5] 2칸씩 뛰어서
# print(a_list[::-2])   # [5,3,1] 역순으로 2칸씩 뛰어서
# print(a_list[::-1])   # [5,4,3,2,1] 역순으로 출력
# print(a_list[:])      # [1,2,3,4,5] 모든 것 출력
# print(a_list)         # [1,2,3,4,5] 모든 것 출력

# a_list = [1,2,3,4,5]
# # 얕은 복사 - 주소값만 복사(한 쪽값 변경하면 영향O)
# b_list = a_list
# a_list[0] = 100
# print(a_list)
# print(b_list)

# # 깊은 복사 - 한 쪽 값을 변경해도 영향X
# b_list = a_list[:]  # :모든 것
# a_list[0] = 100
# print(a_list)
# print(b_list)

# b_list = a_list[::-1]    # 리스트 역순으로 저장
# print(a_list)
# print(b_list)
# a_list[0] = 100
# print(a_list)
# print(b_list)

# 순차 출력
# for i in a_list:
#   print(i)

# # for i in range(len(a_list)):
# #   print(a_list[-(i+1)])

# # 역순으로 출력 5,4,3,2,1
# for i in range(1,len(a_list)+1):
#   print(a_list[-i])



# a_list = [1,2,3.0,"안녕",True, False]

# print(a_list[0])
# print(a_list[3])
# print(a_list[-1])  #거꾸로 첫번째 위치 - False

# a_list = []

# total = 0
# for i in range(100):
#   a_list.append(i+1)
#   total += i+1
# print(total)


# a,b,c,d,e,f,g = 0,0,0,0,0,0,0
# total = 0

# # a,b,c,d,e 의 변수에 숫자를 입력받아 합계를 출력하시오.
# a= int(input("숫자를 입력하세요."))
# b= int(input("숫자를 입력하세요."))
# c= int(input("숫자를 입력하세요."))
# d= int(input("숫자를 입력하세요."))
# e= int(input("숫자를 입력하세요."))
# f= int(input("숫자를 입력하세요."))
# g= int(input("숫자를 입력하세요."))
# total = a+b+c+d+e+f+g
# print("합계 :",total)

# a_list = [0,0,0,0,0,0,0]
# total = 0

# for idx,a in enumerate(a_list):
#   a = int(input(f"{idx+1}번째 숫자를 입력하세요."))
#   total += a

# print("합계 :",total)


# a_list = []
# total = 0

# for i in range(10):
#   j = int(input(f"{i+1}번째 숫자를 입력하세요.>> "))
#   a_list.append(j)
#   total += j

# print("합계 :",total)
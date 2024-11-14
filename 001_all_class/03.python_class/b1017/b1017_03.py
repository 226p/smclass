numbers = [52,273,32,103,90,10,275,1,2,1,2,12]

try:
  print(numbers.index(52))
  print(numbers.index(3))
  print(numbers.index(1))    # find는 ""에서 찾음
  print(numbers.index(32))
except Exception as e:
  print("찾는 번호가 없습니다.",e)






# f = open("b1017/a.txt","w",encoding="utf-8")
# try:
#   f.write("안녕하세요.1\n")
#   f.write("안녕하세요.2\n")
#   f.write({"a":1})
#   f.write("안녕하세요.3")
# except Exception as e:
#   print(e)
# finally:
#   f.close()



# print("1")
# try:             # try구문에 error가 발생해야 except실행시킴
#   print("2")
#   print(3/0)   #--> except로 넘어감
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")
# else:             # try구문에 error가 없으면 실행
#   print("프로그램 에러 발생하지않으면 실행")
#   print("7")
#   print("8")
# finally:             # try구문에 error가 발생해도,안해도 무조건 실행
#   print("9")
#   print("10")


# list_a = [1,2,3,4,5,"홍길동",6,7,8]
# list_b = []
# try:
#   for a in list_a:
#     list_b.append(a**2)
# except Exception as e:     # Exception as e 어떤 부분이 error났는지 설명
#   print(e)
# print(list_b)




# print("프로그램 시작")
# n_str = input("반지름을 입력하세요. >>")

# try:
#   num = int(n_str)
#   #원의 넓이, 원 둘레
#   print("원의 넓이 :",(num**2)*3.14)
#   print("원의 둘레 :",num*2*3.14)
# except Exception as e:
#   print("정수가 아닙니다. 정수를 입력하세요.",e)


#### if구문
# if n_str.isdigit():
#   num = int(n_str)
#   #원의 넓이, 원 둘레
#   print("원의 넓이 :",(num**2)*3.14)
#   print("원의 둘레 :",num*2*3.14)
# else:
#   print("정수가 아닙니다. 정수를 입력하세요.")

#### 예외처리 try - except 구문 사용해서 처리
# try:
# # print("프로그램 시작)     # 구문오류 - 프로그램 실행 전 오류
#   print(list_a)            # 런타임오류 - 프로그램 실행 중 오류
# except:
#   pass

# print("프로그램 종료")
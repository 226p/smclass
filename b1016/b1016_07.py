try:
  a = int(input("숫자를 입력하세요. >>"))
  print("입력된 숫자 : ",a)
except:
  pass


#### try except : 프로그램 예외를 처리하는 명령어
# while True:
#   score = 100
#   print("[ 나눗셈 프로그램 ]")
#   nstr = input("숫자입력")
#   try:                    
#     num = int(nstr)
#     print("입력된 숫자로 100을 나눔:",score/num)
#   except:
#     print("숫자 변환 안됨")
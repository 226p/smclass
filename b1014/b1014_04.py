def calc(n1,n2,op):
  result = 0
  if op == '+':
    result = n1+n2
  elif op == '-':
    result = n1-n2
  elif op == '*':
    result = n1*n2
  else:
    result = n1/n2
  return result

num = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))

op = input("+,-,*,/ 중 하나를 선택하세요.")

print("결과값 :",calc(num,num2,op))
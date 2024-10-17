a = ['1', '홍길동', '89', '57', '14', '160', '53.3333333333', '1']
b = ['1', '89', '57', '14', '160', '53.3333333333', '1']
t_title = ["no","name","kor","eng","math","total","avg","rank"]
c = []
students = []

def f_float(value):
  if value.isdigit():    # 정수인지, 실수 또는 문자열인지 구분
    return int(value)
  else:
    try:
      return float(value)  # 실수일때, 실수로 변환
    except:
      return value         # 문자열일때, 그대로 리턴

for idx,value in enumerate(a):
  c.append(f_float(value))
students.append(dict(zip(t_title,c)))
print(students)


### 숫자로만 구성 - 정수, 실수
for idx,value in enumerate(b):
  if value.isdigit():  # isdigit 정수-True 실수-False
    print(f"{idx}번째 {type(int(value))}")
  else:
    print(f"{idx}번째 {type(float(value))}")

### try-except구문 이용하여 정수,실수 구분
def t_float(n):
  try:
    int(n)
    return True
  except:
    return False
  
for idx,i in enumerate(a):
  if i.isdigit(): 
    print(f"{idx}번째 {i}는 숫자입니다.")
  else:
    print(f"{idx}번째 {i}는 문자입니다.")


# for i in b:
#   if t_float(i): i = int(i)
#   else: i = float(i)
#   c.append(i)
# print(c)



# for i in b:
#   c.append(float(i))
# print(c)



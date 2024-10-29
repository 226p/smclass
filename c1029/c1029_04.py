import oracledb

# db연결 함수 선언
def connections():
  try:
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
  except Exception as e: print("예외발생")
  return conn

conn = connections()
cursor = conn.cursor()

## 이름 검색
# search = input("검색할 이름을 입력하세요. >> ")
# sql = "select * from employees where emp_name like '%a%'"
# cursor.execute(sql)

# sql = "select * from employees where emp_name like :search"
# search = '%'+search+'%'
# cursor.execute(sql,search=search)

num1 = input("얼마 이상을 검색하시겠습니까? >>")
num2 = input("얼마 이하를 검색하시겠습니까? >>")
n_list = [num1,num2]

sql = "select employee_id,emp_name,salary from employees where salary >= :1 and salary <= :2 order by salary"
cursor.execute(sql,n_list)

rows = cursor.fetchall()
title = ['employee_id','emp_name','salary']
a_list = []

for row in rows:
  print(dict(zip(title,row)))
  a_list.append(dict(zip(title,row)))
print(a_list)

conn.close()
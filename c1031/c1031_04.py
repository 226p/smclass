import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

# number -> int 정수형으로 변경 / str은 07,08로 input해야 함
d_day = int(input("입사일 중 원하는 달을 입력하세요. >> "))
# d_day = f"0{d_day}"

cursor = conn.cursor()
sql = "select emp_name,hire_date from employees where substr(hire_date,4,2) >= :d_day"

cursor.execute(sql,d_day=d_day)
rows = cursor.fetchall()

for row in rows:
  print(row)

cursor.close()

import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

cursor = conn.cursor()

num = input("숫자를 입력하세요. >> (a,b,c) ")
# num2 = input("숫자를 입력하세요. >> ")
# num3 = input("숫자를 입력하세요. >> ")
# n_list = [num1,num2,num3]

n_list = num.split(",")


## 1. 문자열함수 : f사용
# sql = f"select * from students where no>={num}"
# cursor.execute(sql)

## 2. execute함수 : 변수 key값 추가
# sql = "select * from students where no>=:no"
# cursor.execute(sql,no=num)


# sql = "select * from students where no in (:no1,:no2,:no3)"
# cursor.execute(sql,no1=num1, no2=num2, no3=num3)

## 3. execute함수 : 리스트 값 전달
# execute 뒤에는 dict,list,tuple타입만 가능
sql = "select * from students where no in (:1,:2,:3)"
cursor.execute(sql,n_list)
# cursor.execute(sql,[num])

rows = cursor.fetchall()
titles = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

for title in titles:
  print(f"{title}",end='\t')
print()
print("-"*80)
for row in rows:
  # print(list(row))
  for i,r in enumerate(row):
    if i == 1:
      print(f"{r:8s}",end='\t')
      continue
    if i == 6:
      print(f"{r:.2f}",end='\t')
      continue
    if i == 8:
      print(r.strftime("%Y-%m-%d"),end='\t')
      continue
    print(r,end='\t')
  print()


conn.close()
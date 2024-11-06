import oracledb

conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

cursor = conn.cursor()

sql = "select * from students"
cursor.execute(sql)

rows = cursor.fetchall()
titles = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
students = []

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
    students.append(list(row))
  print()

print(students)

conn.close()
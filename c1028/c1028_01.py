import oracledb

# oracle(외부)이랑 연결 - sql developer연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")

# 연결확인
print(conn.version)

# sql 실행창 오픈
# cursor = conn.cursor()
# sql = "select count(*) from member"
# cursor.execute(sql)

# # 1개 데이터 검색된 내용 호출
# count1 = cursor.fetchone()
# print(f"개수 : {count1}")

# 여러개 데이터 검색된 내용 호출
cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
  print(row)

# print(rows[0][0],rows[0][1],rows[0][2],rows[0][3])

# 꼭 끊어줘야 함
conn.close()
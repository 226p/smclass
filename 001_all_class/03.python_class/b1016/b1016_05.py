####문서파일 읽기(r),덮어쓰기(w),이어쓰기(a),내용복사해서 쓰기

#### 파일(바이너리파일) 자체 읽어오기
f = open("1.jpg","rb")
fData = f.read()
f.close()
print("파일 읽기 성공!")


#### 파일(바이너리파일) 자체 저장하기
ff = open("c:/down/2.jpg","wb")
len = ff.write(fData)
print(f"파일 크기 : {len} 바이트")
ff.close()



#### txt 파일의 내용 복사
# f = open("students.txt","r",encoding="utf-8")
# ff = open("students2.txt","w",encoding="utf-8")
# while True:
#   line = f.readline()
#   if not line: break
#   ff.write(line)
#   print(line.strip())
# f.close()
# ff.close()
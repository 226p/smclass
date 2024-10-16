#### 파일 with - close() 하지 않아도 됨
with open('aa.txt','w',encoding='utf-8') as f:
  f.write("안녕하세요")


#### a - 파일 쓰기(이어쓰기) : 파일 생성 후 글자입력
# print("[ 메모장 ]")
# while True:
#   data = input("저장하려는 글자를 입력하세요.")
#   f = open('a.txt','a',encoding='utf-8')
#   f.write(data+"\n")
#   f.close()

#### w - 파일 쓰기(덮어쓰기) : 파일 생성 후 글자입력
# f = open('aa.txt','w',encoding='utf-8')
# for i in range(1,11):
#   data = f"안녕하세요. {i}\n"
#   f.write(data)
# f.close()
# print("글쓰기 종료")

#### f = open('aa.txt','w',encoding='utf-8')
# f.write("안녕하세요.1\n")
# f.write("안녕하세요.2\n")
# f.write("안녕하세요.3\n")
# f.close()
# print("글쓰기 종료")

#------------------------------------------------------------------------
##### r 파일읽기
#### read() 한줄씩 읽어오기  (가장 많이씀)
# f = open('a.txt','r',encoding='utf-8')
# for line in f:
#   print(line.strip())
# f.close

#### readlines() 모든 글 읽어오기
# f = open('a.txt','r',encoding='utf-8')
# lines = f.readlines
# for line in lines:
#   print(line.strip())
# print(lines)
# f.close()

#### readline() 한줄씩 읽어오기  (가장 많이씀)
# d = open('b.txt','r',encoding='UTF-8') # 가장 바깥 폴더의 위치에서 파일을 찾음 / utf-8넣어야 한글 읽을 수 있음
f = open('c:/aaa/a.txt','r',encoding='UTF-8')   # 절대경로를 사용
while True:
  line = f.readline()   # 한줄씩읽기
  if not line: break   # 여러줄읽기
  print(line.strip())    # strip() : \n값을 생략, 공백제거 후 출력
f.close()
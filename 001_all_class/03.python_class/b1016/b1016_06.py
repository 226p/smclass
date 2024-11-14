import os

#### 폴더가 없을 시 폴더 생성
if not os.path.exists("c:/bbb"):   # 현재 폴더가 존재하는지 확인
  os.mkdir("c:/bbb")   # 현재 폴더만 생성
  # os.makedirs("c:/ccc/bbb")/   #현재폴더와 하위폴더까지 생성
  print("폴더가 없습니다.")
else:
  print("폴더가 있습니다.")

#### 폴더가 있을때 파일 생성
# f = open("c:/aaa/c.txt","w",encoding="utf-8")
# f.write("안녕하세요")
# f.close()
# 파일읽기 - r

stu_key = ["no","name","kor","eng","math","total","avg","rank"]
students = []

f = open('a.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:break
  # for i,v in enumerate(s):
  #   if i == 1: continue
  #   elif i == 6: s[6]['avg'] = float(s[6]['avg'])
  #   else: s[i] = int(i)
  s = line.strip().split(",")   # 문장 끝 \n 제거 / ,로 구분
  s[0] = int(s[0])
  s[2] = int(s[2])
  s[3] = int(s[3])
  s[4] = int(s[4])
  s[5] = int(s[5])
  s[6] = float(s[6])
  s[7] = int(s[7])
  students.append(dict(zip(stu_key,s)))
f.close()

print(students)
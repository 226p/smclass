students = []
subject = ["번호","이름","국어","영어","수학","합계","평균","등수"]
sub = ["no","name","kor","eng","math","total","avg","rank"]


f = open("b1017/students.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line : break
  s = line.strip().split(",")
  # s[0] = int(s[0])
  # s[2] = int(s[2])
  # s[3] = int(s[3])
  # s[4] = int(s[4])
  # s[5] = int(s[5])
  # s[6] = float(s[6])
  # s[7] = int(s[7])
  for idx,i in enumerate(s):
    if idx == 1 : continue
    elif idx == 6: s[6] = float(i)
    else: s[idx] = int(i)
  students.append(dict(zip(sub,s)))    # 딕셔너리로 타입 변경 후 리스트에 추가
  print(students)
print("프로그램을 종료합니다.")
f.close()


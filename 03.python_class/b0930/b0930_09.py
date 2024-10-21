stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [2,"유관순", 99,99,100,99],[3,"이순신", 100,99,98,99],[4,"김구", 80,100,90,99],[5,"김유신", 80,100,90,99]



print("                    [학생 성적 프로그램]")
print("-"*60)

for s_t in stu_title:
  print("{}".format(s_t), end="\t")
print()


stu = [1,"홍길동", 100,100,100,99]
stu.append(stu[2]+stu[3]+stu[4]+stu[5])
stu.append((stu[2]+stu[3]+stu[4]+stu[5])/4)
for t in stu:
  print("{}".format(t), end="\t")
print()

for u in stu_datas:
  u.append(u[2]+u[3]+u[4]+u[5])
  u.append((u[2]+u[3]+u[4]+u[5])/4)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
    u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7]))
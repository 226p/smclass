students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

# 합계, 평균 추가해서 전체 출력

for i in students:
  i.append(i[2]+i[3]+i[4])
  i.append((i[2]+i[3]+i[4])/3)
  # print(i[0],i[1],i[2],i[3],i[4],i[5],i[6])

print("학번\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*55)

for s in students:
  print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}")
subName = ["국어","영어","수학"]
score = {"국어":100, "영어":95, "수학":80}
# print(score)
# print(score['국어'])
# print(subName[0])
# print(score[subName[0]])

for k,v in score.items():
  print(k,":",v)

for i in subName:
  print(i,":",score[i])

print(f"국어 : {score[subName[0]]}")
print(f"영어 : {score[subName[1]]}")
print(f"수학 : {score[subName[2]]}")


# #--------------------------------------------------------------------
# def gugudan(num):
#   for i in range(2,num+1):
#     print(f"[ {i}단 ]")
#     for j in range(2,9+1):
#       print("{} x {} = {}".format(i,j,i*j))

# print(gugudan)

# nArr = [9,5,8]
# gugudan(9)
# gugudan(5)
# gugudan(7)

# for i in nArr:
#   gugudan(i)
#   print("-"*50)

# def gugudan(st,end):
#   for i in range(st,end+1):
#     print("[ {}단 ]".format(i))
#     for j in range(2,9+1):
#       print("{} x {} = {}".format(i,j,i*j))

# for i in range(2,5+1):
#   print(f"[ {i}단 ]")
#   for j in range(2,9+1):
#     print("{} x {} = {}".format(i,j,i*j))

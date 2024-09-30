a_list = [1,2,3]
print(a_list)
a_list.append(4)   # 배열에 추가하는 방법 append(마지막에 추가),insert(원하는 위치에 추가)
print(a_list)
a_list.append(10)
print(a_list)
a_list.insert(0,50)   # 0번째에 50 추가
print(a_list)
a_list.insert(3,20)
print(a_list)

#del(index 위치에 데이터 삭제), remove(데이터 값으로 삭제)
del a_list[0]
print(a_list)
del a_list[2]
print(a_list)
a_list.remove(4)
print(a_list)
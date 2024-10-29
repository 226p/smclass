title = ['e_id','e_name','salary']
aa =[(196, 'Alana Walsh', 3100.0),
(125, 'Julia Nayer', 3200.0),
(180, 'Winston Taylor', 3200.0),
(194, 'Samuel McCain', 3200.0),
(138, 'Stephen Stiles', 3200.0)]
a_list = []

print(type(aa))

for a in aa:
  print(dict(zip(title,a)))
  a_list.append(dict(zip(title,a)))
print()
print(a_list)



# name = "홍길동"

# print('안녕하세요. 이름은 %s'%name)
# print("Hello my name is {}".format(name))

# a = 1
# b = 2

# a_list = [a,b]
# b_list = [b]
# print(a_list)

# print(type(a_list))
# print(type(b_list))

# a_tuple = (a,b)
# print(type(a_tuple))

## 튜플을 1개만 지정할 때는 뒤에 ,를 넣어야 함
# b_tuple = (a,)
# c_tuple = (a)
# print(b_tuple)
# print(type(b_tuple))  tuple타입
# print(type(c_tuple))  int타입

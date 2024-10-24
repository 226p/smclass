lists = ['10억','9억5,000','11억500','7억','12억5,250']

a = '9억 5,000'

# print(int(b[0])*100000000)
# print(int(b[1].strip().replace(",",""))*10000)
def num_shg(p):
  b = p.split('억')
  f_num = int(b[0])*100000000
  if b[1].strip() != '':
    s_num = int(b[1].strip().replace(",",""))*10000
  else: s_num = 0
  price = f_num+s_num
  return price


for li in lists:
  price = num_shg(li)
  print("금액 :",price)

r_list = list(map(num_shg,lists))
print(r_list)
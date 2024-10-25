a = ["1.7만","3,450","1만","500","1,000"]

def chg(val):
  r_val = 0
  if '만' in val:
    r_val = float(val[:-1])*10000
  else:
    r_val = float(val.replace(",",""))
  return r_val

a_list = list(map(chg,a))
print(a_list)

print(max(a_list))
print(min(a_list))

# a = [1,2,3]
# b = [4,5,6]
# print(a+b)
import datetime

# 현재년도
nowYear = datetime.datetime.now().year
in_year = input("생일입력 : 20020312")

print(f"현재나이 : {nowYear-int(in_year[:4])}")



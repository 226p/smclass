import datetime

today = datetime.datetime.now()
print(today)    # 날짜, 시간, 밀리세컨드

# 날짜 포맷
now_date = today.strftime("%Y-%m-%d")
print(now_date)
now_datetime = today.strftime("%Y-%m-%d %H:%M:%S")
print(now_datetime)   
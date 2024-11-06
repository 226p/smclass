import random
import smtplib
from email.mime.text import MIMEText

# 임시 비밀번호 생성함수 선언

a = random.randrange(0,10000) # 0-9999
ran_num = f"{a:04}"
print(ran_num)




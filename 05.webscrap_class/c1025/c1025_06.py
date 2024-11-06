from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options
import pyautogui
import csv
# email 발송
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

smtpName = "smtp.naver.com"
smtpPort = 587

# id, pw, 받는사람이메일주소

sendEmail = "qkrdnwjd0893@naver.com"
pw = "-"
recvEmail = "sh097b@naver.com"

title = "제목 : 파이썬 이메일보내기 안내"
content = """\
◟(ᵔ ̮ ᵔ)͜   ♡
"""

msg = MIMEMultipart()
msg["Subject"] = title
msg["From"] = sendEmail
msg["To"] = recvEmail
msg.attach(MIMEText(content))

with open("c1025/서현2.jpg","rb") as f:
  attachment = MIMEApplication(f.read())  # 파일첨부
  attachment.add_header('Content-Disposition','attachment',filename = '서현2.jpg')
  msg.attach(attachment)

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()  # 보안연결
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.quit()

print("msg :")
print(msg.as_string)
s.quit

print("메일전송이 완료되었습니다.")






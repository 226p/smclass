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

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text,"lxml")

news_list = []
data = soup.select("ul.rankingnews_list>li")
for idx,d in enumerate(data):
  try:
    title = d.select_one("a").text
    tIme = d.select_one("span.list_time ").text
    # print(f"{title} - {tIme}")
    news_list.append([title,tIme])
  except: pass

with open("c1025/naver_news.csv","w",encoding="utf-8-sig",newline="") as f:
  writer = csv.writer(f)
  for n in news_list:
    writer.writerow(n)

smtpName = "smtp.naver.com"
smtpPort = 587

sendEmail = "qkrdnwjd0893@naver.com"
pw = "-"
recvEmail = "qkrdnwjd0893@naver.com"

title = "제목 : 파이썬 이메일보내기 안내"
content = """\
◟(ᵔ ̮ ᵔ)͜   ♡
"""

msg = MIMEMultipart()
msg["Subject"] = title
msg["From"] = sendEmail
msg["To"] = recvEmail
msg.attach(MIMEText(content))

with open("c1025/naver_news.csv","rb") as f:
  attachment = MIMEApplication(f.read())  # 파일첨부
  attachment.add_header('Content-Disposition','attachment',filename = 'naver_news.csv')
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

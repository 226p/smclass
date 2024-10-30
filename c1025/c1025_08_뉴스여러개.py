from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# smtpName = "smtp.naver.com"
# smtpPort = 587
# # 자신의 네이버메일주소, pw, 받는사람이메일주소
# sendEmail = "rkwhkehd3927@naver.com"
# pw = "MDHHDW1ZDM8R" # 자기거
# recvEmail = "qkrdnwjd0893@naver.com"
# recvEmail2 = "sh097b@naver.com"
# title = "제목 : 파이썬 이메일보내기 안내"
# content = "저도 이메일을 보내고 싶습니다."
# # 설정
# msg = MIMEMultipart()
# msg['Subject'] = title
# msg['From'] = sendEmail
# msg['To'] = recvEmail
# msg.attach(MIMEText(content))


with open("c1025/news.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,"lxml")
data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking")
lists = data.select("div.rankingnews_box")

n_list = []

for idx, area in enumerate(lists):
  name = area.select_one("strong").text.strip()
  print()
  print("언론사 : ",name)
  title = area.select("div.list_content > a")
  for i,t in enumerate(title):
    t = t.text.strip()
    print(f"{idx*12+i+1}위 - {t}")
    n_list.append([idx*5+i+1,name,t])

print(n_list)

with open("c1025/naver_nlist.csv","w",encoding="utf-8-sig",newline="") as f:
  writer = csv.writer(f)
  for n in n_list:
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

with open("c1025/naver_nlist.csv","rb") as f:
  attachment = MIMEApplication(f.read())  # 파일첨부
  attachment.add_header('Content-Disposition','attachment',filename = 'naver_nlist.csv')
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
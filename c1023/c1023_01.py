import os
import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")

f = open('c1023/stocks.csv','w',encoding='utf-8-sig',newline="")
writer = csv.writer(f)


### 1. 상단 타이틀
st_list = [st.text for st in stocks[0].select("th")]   # 리스트 내포 (항목 12개)
writer.writerow(st_list)

### 2. 주식
# print(sto_list)

for sto in stocks:
  sts = sto.select("td")
  if len(sts) <= 1 : continue
  sto_list = [ st.text.strip().replace("\t","").replace("\n","")  for st in sts ]
  writer.writerow(sto_list)   # csv파일에 리스트타입 저장
  print(sto_list)

f.close()

print("완료")







### list 생성
# sts = stocks[0].select("th")
# st_list = []
# for st in sts:
#   st_list.append(st.text)
# print(st_list)
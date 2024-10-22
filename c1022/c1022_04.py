import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()   # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
title = soup.select("tr.type1>th")
sib = soup.select_one("tr.type1").find_next_sibling("tr")

print(sib.find_next_sibling("tr"))


with open("a.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

for t in title:
  print(t.text,end='\t')
print()
print("-"*100)


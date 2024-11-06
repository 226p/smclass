import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()   # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

with open("a.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01
data = soup.select_one("#frm > div > table > tbody")
t_centers = data.select("div.wrap_song_info")

# print(data.select_one("div.wrap_song_info"))
for idx,t in enumerate(t_centers):
  for i in range(len(t)):
    if not None: print(t.select_one("span.checkEllipsis>a"))
  # print(f"{idx+1}위 {t.select_one("a").next} - {t}")




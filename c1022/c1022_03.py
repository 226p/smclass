import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()   # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
sum = 0

aside = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular")
pops = aside.select("tbody>tr")
print(f"[ {aside.select_one("span").text} ]")
# print(len(pops))

for i,p in enumerate(pops):
  print()
  print(f"회사명 : {p.select_one("a").text}")
  print(f"현재가 : {p.select_one("td").text}")

  ## next_sibling : 형제관계, find_next_sibling() : 형제관계 중 ()검색
  sps = p.select_one("td").find_next_sibling("td").select("span")
  tit = ["변동","변동액"]
  for idx,sp in enumerate(sps):
    print(tit[idx],":",sp.text.strip())
  # print(f"변동 : {p.select_one("td").find_next_sibling("td").select_one("span").text}")
  # print(f"변동 : {p.select_one("td").find_next_sibling("td").select_one("span").next.next.next.strip()}")
  a = p.select_one("td").text.replace(",","")
  sum += int(a)
print(f"{sum:,}")
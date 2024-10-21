import requests
from bs4 import BeautifulSoup

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


title = soup.find("div",{"id":"bestPrdList"})

print(title.h3.text)
# print(title.find("div",{"class":"pname"}).p.text)

best = soup.find("div",{"id":"bestPrdList"}).find("ul",{"class":"cfix"})
bestLists = best.find_all("li")

for i,bestList in enumerate(bestLists):
  price = bestList.find("strong",{"class":"sale_price"})
  print(f"{i+1}. {bestList.p.text} : {price.text}원")

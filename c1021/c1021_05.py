import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

print(soup.find("div",{"class":"rankingnews_box"}))
print(len(soup.find_all("div",{"class":"rankingnews_box_wrap"})))

# find() : 특정위치의 태그를 1개 검색하며 태그와 속성을 가지고 출력해줌
rankingnews_wrap = soup.find("div",{"class":"rankingnews_box_wrap"})
# find_all() : 특정위치의 태그를 여러개 검색
rankingnews_boxs = rankingnews_wrap.find_all("div",{"class":"rankingnews_box"})
newsLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
# print(len(newsLists))
print(len(rankingnews_boxs))
# print(soup.find("strong",{"class":"rankingnews_name"}).text)

for newList in newsLists:
  print(newList.find("strong",{"class":"rankingnews_name"}).text)

with open("c1021/a.html","w",encoding="utf-8") as f:
  f.write()
  

# a = "안녕하세요. 반갑습니다. 파이썬 수업입니다."

# search = "파이썬"
# print(a.find(search))
# print(a[a.find(search):a.find(search)+3])
# print(a.find("자바"))
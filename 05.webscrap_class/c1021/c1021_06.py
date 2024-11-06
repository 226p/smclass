import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


rankingnews_wrap = soup.find("div",{"class":"rankingnews_box_wrap"})
# find_all() : 특정위치의 태그를 여러개 검색
rankingnews_boxs = rankingnews_wrap.find("div",{"class":"rankingnews_box"})
newsLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find("div",{"class":"rankingnews_box"})

print(newsLists.next)    # next :검색테그 다음 줄에 오는 태그를 찾아줌
print(newsLists.next_sibling.next_sibling)   # next_sibling : 검색태그의 형제관계의 다음태그를 찾아줌
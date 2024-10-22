import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()   # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

# print(res.text)  # 타입 str
# print(soup.prettify())  # html,css 파싱(정리)되어서 출력

# 태그를 활용한 검색기능 : find, find_all <-> select_one, select

# print(soup.find("h2",{"class":"rankingnews_tit"}).text)
# print(soup.select_one("h2.rankingnews_tit").text)
# print(soup.select_one("div#header"))


data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking")
news_lists = data.select("div.rankingnews_box")
#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking

print("갯수 :",len(news_lists))
for news in news_lists:
  print()
  print("언론사 이름 : ",news.select_one("strong.rankingnews_name").text)
  news_lists = news.select("ul.rankingnews_list>li")
  for idx,news_list in enumerate(news_lists):
    print(f"{idx+1} : ",news_list.select_one("div.list_content>a").text)




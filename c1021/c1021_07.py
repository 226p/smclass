import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

newsLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
# print("타이틀 :",soup.find("strong",{"class":"rankingnews_name"}).text)


for idx,newList in enumerate(newsLists):
  print()
  print(f"{idx+1}. 타이틀 : ",newList.find("strong",{"class":"rankingnews_name"}).text)

  rank_list = newList.find("ul",{"class":"rankingnews_list"})
  tLists = rank_list.find_all("li")

  for i,t in enumerate(tLists):
    print(i+1,":",t.find("a").text)
print("갯수 :",len(tLists))


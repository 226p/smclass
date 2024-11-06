import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

pop = soup.find("div",{"class":"hot_issue"})
music = pop.find("li",{"class":"issue_list04"})
muSic = music.find_all("dl")

print(pop.find("span",{"class":"title_link"}).text)
for i,m in enumerate(muSic):  # --> 이미지 저장하기~
  title = m.find("span",{"class":"title"}).text
  ellipsis = m.find("span",{"class":"ellipsis"}).text
  print(f"{i+1}. {ellipsis}-{title}")

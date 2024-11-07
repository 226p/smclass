from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

#---------------------------------------------------request로 뽑기
# url = "https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,'lxml')
#---------------------------------------------------selenium으로 뽑기
# for i in range(4):
#   url = f"https://search.daum.net/search?w=tot&q=202{i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

#   browser = webdriver.Chrome()
#   time.sleep(3)
#   browser.get(url)
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source,'lxml')
  
#   with open(f"202{i}년_다음영화순위.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

#---------------------------------------------------저장한 파일 select로 뽑기
t_list = ["제목","누적 관객수"]
for i in range(4):
  a_list = []
  with open(f"202{i}년_다음영화순위.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

  data = soup.select("#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc > ul >li")

  for idx,d in enumerate(data):
    title = d.select_one("div.item-title > c-title > strong > a").text.strip()
    view = d.select_one("div.item-contents > c-contents-desc > p").text.strip()
    if '만' in view:
      view = int(view[3:-2].replace(",",""))*10000
    else: int(view.replace(",",""))
    m_list = [title,view]


    a_list.append(dict(zip(t_list,m_list)))
    # a_list.append([title,view])
    print(a_list)

  with open(f"d1106/daum_movie202{i}.csv","w",encoding="utf-8-sig",newline="") as f:
    writer = csv.writer(f)

    writer.writerow(a_list)
      

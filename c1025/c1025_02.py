from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options
import pyautogui
import csv

def chg(val):
  r_val = 0
  if '만' in val:
    r_val = float(val[:-1])*10000
  else:
    r_val = float(val.replace(",",""))
  return r_val

# browser = webdriver.Chrome()
# browser.maximize_window()

search_list = []
for i in range(5):
  # url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i+1}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"

  # time.sleep(3)
  # browser.get(url)
  # time.sleep(10)
  # while True:
  #   prev_height = browser.execute_script("return document.body.scrollHeight")
  #   browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  #   time.sleep(5)
  #   curr_height = browser.execute_script("return document.body.scrollHeight")
  #   if prev_height == curr_height: break
  #   prev_height = curr_height

  # input("최신화 완료! ENTER 입력>> ")

  # soup = BeautifulSoup(browser.page_source,"lxml")

  # with open(f"c1025/naver_shop0{i+1}.html","w",encoding="utf-8") as f:
  #   f.write(soup.prettify())

####제목,금액,평점,평가수,찜 ~ 정보 1p~5p가져오기 / 평점 4.8↑ 평가수 1000↑ csv타입 저장 후 출력

  with open(f"c1025/naver_shop0{i+1}.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

  # soup.select_one("#content").next_sibling
  data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx>div")
  lists = data.select("div.product_info_area__xxCTi")

  search_list = []
  for idx,l in enumerate(lists):
    try:
      name = l.select_one("div.product_title__Mmw2K>a").text.strip()
      price = int(l.select_one("span.price_num__S2p_v>em").text.strip().replace(",",""))
      rating = float(l.select_one("span.product_grade__IzyU3").text.strip().replace(" ","").replace("\n","")[2:])
      num = l.select_one("em.product_num__fafe5").text.strip()[1:-1]
      num = int(chg(num))
      zzim = int(l.select_one("span.product_num__fafe5").text.strip())

      if rating>=4.8 and num>=1000:
        print(f"{(i*44)+idx+1}. 상품명 : {name}")
        print(f"  - 가격 : {price}")
        print(f"  - 평점 : {rating}")
        print(f"  - 평가수 : {num}")
        print(f"  - 찜 : {zzim}")
        search_list.append([name,price,rating,num,zzim])
    except: pass

  print(len(lists))

  # print(search_list)
  # with open("c1025/search_list.csv","a",encoding="utf-8-sig",newline="") as f:
  #   writer = csv.writer(f)

  #   for l in search_list:
  #     writer.writerow(l)





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


search_list = []
for i in range(5):
  with open(f"c1025/naver_shop0{i+1}.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

  data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx>div")
  lists = data.select("div.product_info_area__xxCTi")+data.select("div.adProduct_info_area__dTSZf")

  for idx,l in enumerate(lists):
    if 'xxCTi' in str(l['class']):
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

    else:
      try:
        name1 = l.select_one("div.adProduct_title__amInq>a").text.strip()
        price1 = int(l.select_one("span.price_num__S2p_v>em").text.strip().replace(",",""))
        rating1 = float(l.select_one("span.adProduct_rating__PaMzh").text.strip().replace(" ","").replace("\n","")[2:])
        num1 = l.select_one("em.adProduct_count__EDNPm").text.strip()[1:-1]
        num1 = int(chg(num1))
        zzim1 = int(l.select_one("span.adProduct_num__t7R1x").text.strip())

        if rating1>=4.8 and num1>=1000:
          print(f"{(i*44)+idx+1}. 상품명 : {name1}")
          print(f"  - 가격 : {price1}")
          print(f"  - 평점 : {rating1}")
          print(f"  - 평가수 : {num1}")
          print(f"  - 찜 : {zzim1}")
          search_list.append([name1,price1,rating1,num1,zzim1])
      except: pass

  # print(search_list)
  # with open("c1025/search_list_광고포함.csv","a",encoding="utf-8-sig",newline="") as f:
  #   writer = csv.writer(f)

  #   for l in search_list:
  #     writer.writerow(l)




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

# url = "https://new.land.naver.com/complexes/107929?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL"

# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# time.sleep(1)
# pyautogui.moveTo(1270,550)
# time.sleep(1)
# pyautogui.moveTo(1270,480)
# time.sleep(1)
# pyautogui.moveTo(390,800)
# pyautogui.click()
# # all_height = browser.execute_script("return document.body.scrollHeight")
# # print("화면 전체 높이 :",all_height)
# prev_height = browser.execute_script("return articleListArea.scrollHeight")
# print("화면 높이 :",prev_height)
# while True:
#   pyautogui.scroll(-prev_height)
#   time.sleep(2)
#   curr_height = browser.execute_script("return articleListArea.scrollHeight")
#   if prev_height == curr_height: break
#   prev_height = curr_height

# soup = BeautifulSoup(browser.page_source,"lxml")
# data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div")
# with open("c1024/naver.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())

# input("enter입력 >>")

with open("c1024/naver.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,"lxml")

data = soup.select("div.item_inner")
print(len(data))

def num_chg(p):
  a = p.split('억')
  f_num = int(a[0])*100000000
  if a[1] != '':
    s_num = int(a[1].strip().replace(",","").replace("\n","").replace("/",""))*10000
  else: s_num = 0
  price = f_num+s_num
  return price

num_m = 0
num_j = 0
num_w = 0
search_list = []
s_list = []
for idx,d in enumerate(data):
  address = d.select_one("span.text").text.strip()
  tYpe = d.select_one("span.type").text.strip()
  price = d.select_one("span.price").text.strip()
  spec = d.select_one("span.spec").text.strip()
  if tYpe.find("매매"):
    if tYpe.find("전세"):
      print(f"{idx+1}. 제외")
      num_w += 1
      pass
    else:
      price = num_chg(price)
      s_list.append([address,tYpe,price,spec])
      num_j += 1
  else:
    price = num_chg(price)
    print(f"{idx+1}. 이름 : {address}")
    print(f"   - {tYpe} {price}")
    print(f"   - {spec}")
    search_list.append([address,tYpe,price,spec])
    num_m += 1


search_list.sort(key=lambda x:x[2])
s_list.sort(key=lambda x:x[2])
top_p = search_list[:5]
top_pp = s_list[:5]

print(f"매매 TOP5 : {top_p}")
print(f"전세 TOP5 : {top_pp}")

print(num_j) # 전세 갯수
print(num_m) # 매매 갯수
print(num_w) # 월세 갯수
print(len(data)) # 총 갯수
  




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


num = 0
s_list = []
m84_list = []
m59_list = []
m101_list = []
m72_list = []
j_list = []

num84 = 0
num59 = 0
num101 = 0
num72 = 0
for idx,d in enumerate(data):
  address = d.select_one("span.text").text.strip()
  tYpe = d.select_one("span.type").text.strip()
  price = d.select_one("span.price").text.strip()
  spec = d.select_one("span.spec").text.strip()
  if tYpe.find("매매") == -1:
    if tYpe.find("전세") == -1:
      pass
    else:
      price = num_chg(price)
      s_list.append([address,tYpe,price,spec])
  else:
    if spec.find("84m²") == -1:
      if spec.find("59m²") == -1:
        if spec.find("101m²") == -1:
          if spec.find("72m²") == -1:
            pass
          else:
            price = num_chg(price)
            m72_list.append([address,tYpe,price,spec])
            num72 += 1
        else:
          price = num_chg(price)
          m101_list.append([address,tYpe,price,spec])
          num101 += 1
      else:
        price = num_chg(price)
        m59_list.append([address,tYpe,price,spec])
        num59 += 1
    else:
      price = num_chg(price)
      m84_list.append([address,tYpe,price,spec])
      num84 += 1


s_list.sort(key=lambda x:x[2])
m84_list.sort(key=lambda x:x[2])
m59_list.sort(key=lambda x:x[2])
m101_list.sort(key=lambda x:x[2])
m72_list.sort(key=lambda x:x[2])
top_pp = s_list[:5]
top_84 = m84_list[:5]
top_59 = m59_list[:5]
top_101 = m101_list[:5]
top_72 = m72_list[:5]

print(f"매매(84m²) TOP5 : {top_84}")
print()
print(f"매매(59m²) TOP5 : {top_59}")
print()
print(f"매매(101m²) TOP5 : {top_101}")
print()
print(f"매매(72m²) TOP5 : {top_72}")
print()
print(f"전세 TOP5 : {top_pp}")

print(num84)
print(num59)
print(num101)
print(num72)




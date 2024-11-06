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

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

### 노트북으로 검색된 사이트에서 1,2,3페이지 자료 저장
# for i in range(3):
#   url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i+1}"

#   browser = webdriver.Chrome(options=options)
#   time.sleep(3)
#   browser.get(url)
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source,"lxml")

#   with open(f"c1024/gmarket{i+1}.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

#   browser.get_screenshot_as_file(f"gamrket{i+1}.png")
  
# input("enter 입력>> ")

fail_num = 0
true_num = 0
ex_num = 0
search_list = []
lists = []

for i in range(3):
  with open(f"c1024/gmarket{i+1}.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

  data = soup.select("div.box__information")

  # print(len(data))
  for idx,d in enumerate(data):
    try:
      name = d.select_one("span.text__item").text.strip()
      price = int(d.select_one("strong").text.strip().replace(",",""))
      rating = int(d.select_one("span.image__awards-points").text.strip()[4:-6])
      num = int(d.select_one("li>span.text").text.strip().replace(" ","").replace("\n","")[1:-1])
      search_list.append([i+1,name,price,rating,num])
      if num<100 or rating<95 or price>1500000:
        print(f"{i+1}-{idx+1}번 제외")
        fail_num += 1
        continue
      print(f"{i+1}-{idx+1}. 상품명 : {name}")
      print(f" - 금액 : {price}원")
      print(f" - 만족도 : {rating}%")
      print(f" - 평가수 : {num}명")
      lists.append([i+1,name,price,rating,num])
      true_num += 1
    except: 
      ex_num += 1
      search_list.append([i+1,name,price,rating,num])
      pass
  
lists.sort(key=lambda x:x[2])
top_p = lists[:1]
lists.sort(key=lambda x:x[3],reverse=True)
top_r = lists[:1]

print(f"[ 검색정보 ]")
print(f"1. 조건에 맞는 갯수 : {true_num}")
print(f"2. 조건에 맞지 않는 갯수 : {fail_num}")
print(f"3. 예외처리 갯수 : {ex_num}")
print(f"4. 총 갯수 : {len(search_list)}")
print(f"5. 평점1위 : {top_r}")
print(f"6. 금액 최저가 : {top_p}")






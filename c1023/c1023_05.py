from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# for i in range(5):
#   url = f"https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&autoKeyword=&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=true&page={i+1}"

#   browser = webdriver.Chrome()  # .exe파일 외부에 있으면 ("c:/down/chromedriver-win64")안에 주소를 지정해줘야 함
#   time.sleep(2)
#   browser.get(url)
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source,"lxml")

#   # 파일 저장하기
#   with open(f"c1023/yeogi{i+1}.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

## 파일 불러오기 - BeautifulSoup으로 파싱
for i in range(5):
  with open(f"c1023/yeogi{i+1}.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,'lxml')

  data = soup.select_one("#__next > div > main > section > div.css-1qumol3")
  sells = data.select("a")

  print("[ 강릉숙소 ]")
  for idx,sell in enumerate(sells):
    try:
      rating = float(sell.select_one("span.css-9ml4lz").text.strip())
      num = int(sell.select_one("span.css-oj6onp").text.strip()[:-4].replace(",",""))
      price = int(sell.select_one("span.css-5r5920").text.strip().replace(",",""))
      link = sell['href']
      # img = sell.select_one("img")['src']
      if rating<9.0 or num<500 or price>120000 : 
        print(f"{(i*20)+idx+1}번 제외")
        continue
      print(f"{idx+1}.")
      print(f"숙소명 : {sell.select_one("h3").text.strip()}")
      print(f"평점 : {rating}")
      print(f"평가수 : {num}")
      print(f"금액 : {price}원")
      # print(f"이미지 : {img}")
      print(f"링크주소 : https://www.yeogi.com{link}")
      print()
    except Exception as e:
      # print(i,"예외처리 ",e)
      pass


# time.sleep(100)

















#------------------------------------------------------------------------
#### requests로 정보 가져오기
#  headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

# res = requests.get(url,headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,"lxml")

# with open("c1023/yeogi1.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())

# data = soup.select_one("#__next > div > main > section > div.css-1qumol3")
# print(data)
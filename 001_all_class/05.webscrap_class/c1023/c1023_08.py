from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

url = "https://flight.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()     # 창 최대화
browser.get(url)

# 출발지 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()

time.sleep(random.randint(2,5))
# 출발지 입력(김포)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[1]/div/input').send_keys("김포")

time.sleep(random.randint(2,5))
# 출발지 선택(김포)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b').click()

time.sleep(random.randint(2,5))
# 도착지 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()

time.sleep(random.randint(2,5))
# 도착지 입력(제주)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[1]/div/input').send_keys("제주")

time.sleep(random.randint(2,5))
# 도착지 선택(제주)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a/b').click()

time.sleep(random.randint(2,5))
# 가는 날 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()

time.sleep(random.randint(2,5))
# 가는 날 선택(11.6)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button').click()

time.sleep(random.randint(2,5))
# 오는 날 선택(11.9)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button').click()

time.sleep(random.randint(2,5))
# 인원 선택
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()

time.sleep(random.randint(2,5))
# 인원 추가
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()

time.sleep(random.randint(2,5))
# 항공권 검색
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()

time.sleep(random.randint(2,5))
# 데이터를 검색하는 동안 대기상태
time.sleep(7)

## 화면 대기 함수
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC 

## 화면에 찾으려고 하는 <html>요소가 있는지 확인
# elem = WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))
## 화면 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")  # 현재 스크롤 위치 검색
print("최초 높이 :",prev_height)
time.sleep(random.randint(2,5))
while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")   # 스크롤 내리기
  time.sleep(2) # 다른정보가 추가될때까지 대기
  # 높이 확인 - 2000
  curr_height = browser.execute_script("return document.body.scrollHeight")   # 높이 확인
  if prev_height == curr_height:
    break
  prev_height = curr_height
  print("현재 높이 :",curr_height)

####----------------------------------------------------------------------------------
# 데이터 가져와서 처리(BeautifulSoup 데이터 처리)
soup = BeautifulSoup(browser.page_source,"lxml")

with open("c1023/flight.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

input("enter키를 입력하면 프로그램이 종료됩니다.")
browser.quit()

time.sleep(100)




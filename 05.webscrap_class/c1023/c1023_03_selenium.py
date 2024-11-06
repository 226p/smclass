import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get("https://www.naver.com")

# html 위치 찾기 - requests.select
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')  # class로 찾기
# elem = browser.find_element(By.ID,'query')  # id로 찾기
elem.click()                   # 클릭
browser.back()                 # 페이지 뒤로가기
browser.forward()              # 페이지 앞으로 가기
browser.refresh()              # 페이지 새로고침
elem.send_keys('네이버 영화')   # 글자 입력
elem.send_keys(Keys.ENTER)     # 엔터키 입력
browser.switch_to.window(browser.window_handles[1])  # 다른창 이동

time.sleep(100)  # 10초 지연시켜줌
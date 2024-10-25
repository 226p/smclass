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

# url = "https://www.naver.com/"

# browser = webdriver.Chrome()
# time.sleep(1)
# browser.maximize_window()
# time.sleep(1)
# browser.get(url)

# elem = browser.find_element(By.XPATH,'//*[@id="query"]')
# elem.send_keys("네이버 쇼핑")
# time.sleep(2)
# elem.send_keys(Keys.ENTER)
# time.sleep(2)

# elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a').click()
# time.sleep(2)

# # 새로운 탭 이동
# browser.switch_to.window(browser.window_handles[1])
# elem = browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
# time.sleep(2)
# elem.send_keys("무선마우스")
# elem.send_keys(Keys.ENTER)
# time.sleep(3)

# while True:
#   prev_height = browser.execute_script("return document.body.scrollHeight")
#   browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#   time.sleep(2)
#   curr_height = browser.execute_script("return document.body.scrollHeight")
#   if prev_height == curr_height: break
#   curr_height = prev_height

# print("스크롤 최신화 완료 !")
# input("ENTER 입력 >>")


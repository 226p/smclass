import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.daum.net/')

elem = browser.find_element(By.ID,'q')
elem.send_keys("주식정보")
time.sleep(3)
elem.send_keys(Keys.ENTER)

browser.get("https://www.naver.com")
elem = browser.find_element(By.ID,"query")
elem.send_keys("주식정보")
elem.send_keys(Keys.ENTER)

time.sleep(100)
















###-----------------------------------------------------------------------------
# import time
# import random

# a = [0]*100
# for i in range(100):
#   a[i] = i


# b = [i for i in range(100)]
# for i in b: 
#   print(i)
#   time.sleep(random.uniform(1,3))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

url = "https://www.daum.net/"

browser = webdriver.Chrome()
browser.get(url)

id = "aaa"
pw = "111"
input_js = f'document.getElementById("loginId--1").value="{id}";document.getElementById("password--2").value="{pw}";'

elem = browser.find_element(By.CLASS_NAME,"btn_login")
elem.click()
time.sleep(random.randint(2,5))

browser.execute_script(input_js)  
time.sleep(random.randint(2,5))

elem = browser.find_element(By.CLASS_NAME,"btn_g highlight submit")
elem.click()
time.sleep(random.randint(2,5))
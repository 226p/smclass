from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

with open("c1023/flight.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,"lxml")


data = soup.select("div.domestic_prices__WBiv_>div.domestic_item__5CAye")
lists = soup.select("div.domestic_inner__8geIy>div.domestic_item__5CAye")
print(len(lists))
for d in data:
  print(d.select_one("b.domestic_price__SAqlB>i").text.strip())
# for l in lists:
#   print(l.select_one("b.airline_name__0Tw5w"))

# print(data.select_one("b.domestic_price__SAqlB>i").text.strip())

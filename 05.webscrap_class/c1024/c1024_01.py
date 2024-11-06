from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random

url = "https://www.yanolja.com/?trackcode=mkt_google_sa&utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-298391364620&gad_source=1&gclid=EAIaIQobChMIzI2v5eKliQMVx14PAh0RzCZyEAAYASAAEgKNpfD_BwE"


# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# # 검색창 선택
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]').click()
# time.sleep(2)

# # 날짜 선택
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()
# time.sleep(2)

# # 입실 날짜 선택(11/11)
# elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
# time.sleep(2)

# # 퇴실 날짜 선택(11/13)
# elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()
# time.sleep(2)

# # 확인 클릭
# elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button').click()
# time.sleep(2)

# # 목적지 입력(강릉호텔)
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
# elem.send_keys("강릉호텔")
# time.sleep(2)
# elem.send_keys(Keys.ENTER)

# # 자동 실행 시 로딩 대기
# ## 화면의 호텔 검색내용이 뜰 때까지 대기, 최대30초까지 대기
# WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

# # 화면 스크롤 내리기 반복
# ## execute_script : 자바스크립트 실행구문(함수)
# prev_height = browser.execute_script("return document.body.scrollHeight")
# while True:
#   browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#   time.sleep(1)
#   # 페이지가 로딩되면서 길어진 길이를 다시 가져오기
#   curr_height = browser.execute_script("return document.body.scrollHeight")
#   # 페이지 스크롤 길이 확인
#   if prev_height == curr_height: break
#   # 길이가 더 길어졌으면, 이전길이에 현재길이 입력시킴
#   prev_height = curr_height

# print("스크롤 내리기 완료")

# soup = BeautifulSoup(browser.page_source,"lxml")

## html 저장하기
# with open("c1024/yanolja.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())

# 파일 불러와서 soup으로 파싱
with open("c1024/yanolja.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,"lxml")

# input("Enter키를 입력하면 완료됩니다.")
chk = 0
fail_num = 0
true_num = 0
ex_num = 0
search_list = []


data = soup.select("div.PlaceListItemText_area__3l67D")
for i,d in enumerate(data):
  try:
    list = d.select_one("strong").text.strip()
    rating = float(d.select_one("span.PlaceListScore_rating__3Glxf").text.strip())
    price = int(d.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK").text.strip().replace(",",""))
    if rating<4.8 or price>170000 :
      print(f"{i+1}. 제외")
      fail_num += 1
      continue
    print(f"{i+1}. 호텔명 : {list}")
    print(f"   - 금액 : {price}")
    print(f"   - 평점 : {rating}")
    search_list.append([i+1,list,rating,price])
    true_num += 1
  except:
    ex_num += 1
    pass
search_list.sort(key=lambda x:x[2],reverse=True)   # 평점 역순 정렬
top_r = search_list[:1]  # 평점 상위 5개만 출력
search_list.sort(key=lambda x:x[3])   # 금액 순차 정렬
top_p = search_list[:1]
# print(search_list[:5])  # 금액 최저가 5개만 출력

print("[ 검색정보 ]")
print(f"1. 조건에 맞는 갯수 : {true_num}")
print(f"2. 조건에 맞지 않는 갯수 : {fail_num}")
print(f"3. 예외처리 갯수 : {ex_num}")
print(f"4. 총 갯수 : {len(data)}")
print(f"5. 평점1위 : {top_r}")
print(f"6. 금액 최저가 : {top_p}")




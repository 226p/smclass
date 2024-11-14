import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

with open("c1021/1.html","w",encoding="utf-8") as f:
  f.write(res.text)

  # html,css 정보를 가진 소스로 변경
soup = BeautifulSoup(res.text,"lxml")   # str -> html태그,css태그 사용될 수 있는 상태로 변경

print(soup.title)                # title태그 : 제일먼저 찾아지는 것을 출력
# print(soup.title.text())       # title태그 안에 문자열 출력
print(soup.title.get_text())     # title태그 안에 문자열 출력

print(soup.a)            # a태그의 첫번째 것 가져오기
print(soup.a.next.text)  # next 다음태그 가져오기
print(soup.a.attrs)     # 태그의 속성값 가져오기 : 딕셔너리 타입
print(soup.a["href"])   # a태그의 href 속성값 가져오기

# print(soup.find("div",attrs={"id":"header"}))   # 특정정보 출력
# print(soup.find("div",{"id":"header"}))  
# print(soup.find("div",{"class":"rankingnews_box"}).text)
# print(len(soup.find_all("div")))    # 모든 div타입 출력
print(type(soup.find_all("div")))     # ResultSet : 객체의 리스트(len이 있음)
print(len(soup.find_all("div",{"class":"rankingnews_box"})))


# print("없는 태그 :",soup.titletitletitle)   # 없는 태그 입력시 None
# print("없는 태그 :",soup.titletitletitle.get_text)   # 없는 태그 입력시 error

# with open("c1021/2.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())   # soup.prettify() : 소스가 정리되어 저장

print("완료")

# print(res.text)
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()   # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")

### 상단 타이틀 출력
tits = stocks[0].select("th")
title = []
st_lists = []

f = open("c1022/stock.tct","w",encoding="utf-8")

for t in tits:
  title.append(t.text)
  print(t.text,end='\t')
print()
print("-"*100)

f.write(','.join(title)+"\n")

### 하단(주식 5개) 출력 / 출력과 동시에 리스트 추가
for i in range(2,50):
  st_list = []
  sts = stocks[i].select("td")
  if len(sts) <= 1 : continue   # td가 1개 이하이면 skip
  for idx,st in enumerate(sts):
    s = ""
    if idx == 4:   # 4번째 빈공간 없애는 방법
     s = st.select_one("span").text
     s += st.select_one("span").next.next.next.next.strip()
     print(s,end="")    
     print(st.select_one("span").next.next.next.next.strip(),end='\t')
    else:
      s = st.text.strip()
      print(st.text.strip(),end='\t')
    st_list.append(s)
  f.write(','.join(st_list)+"\n")
  st_lists.append(st_list)

f.close

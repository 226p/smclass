import os
import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

with open("a.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

### 내가 한 것
# data = soup.select_one("#productList>li")

# print(f"상품명 : {data.select_one("div.name").text}")
# print(f"가격 : {data.select_one("strong.price-value").text}원")
# print(f"평점 : {data.select_one("div.rating-star").text}")
# print(f"이미지링크 : https:{data.select_one("img")['src']}")


data = soup.select_one("#productList")
lists = data.select("li")

# 금액 90↑, 평점 4.5↑, 평가수 100↑

n_lists = []
for idx,list in enumerate(lists):
  n_lists = []
  try:
    link = "https://www.coupang.com"+list.select_one("a")['href']
    name = list.select_one("div.name").text
    price = int(list.select_one("strong.price-value").text.replace(",",""))
    rating = float(list.select_one("em.rating").text)
    num = int(list.select_one("span.rating-total-count").text[1:-1])
    img = "https:"+list.select_one("img")['src']
    if price>=900000 and rating >= 4.5 and num >= 100:
      n_lists = []
      print(f"{idx+1}. 링크 : {link}")
      print(f"  - 상품명 : {name}")
      print(f"  - 가격 : {price:,}원")
      print(f"  - 평점 : {rating}")
      print(f"  - 평가수 : {num}")
      print(f"  - 이미지링크 : {img}")
      print()
      n_list = [link,name,price,rating,num,img]
      n_lists.append(n_list)
    else:
      print(f"[{idx} 번째 ] : 제외")
  except Exception as e:
    print(f"{idx}:에러",e)
    pass

print(n_lists)  # 왜 안 넣어지는지~확인요망

# while True:
#   print("[ 노트북 비교 ]")  
#   print("1. 금액정렬")  
#   print("2. 금액역순정렬")  
#   print("3. 평점정렬")  
#   print("4. 평점역순정렬")  
#   print("0. 종료")
#   print("-"*50)  
#   choice = input("원하는 번호를 입력하세요.")  

#   if choice == "1":
#     # n_lists.sort()
#     pass
#   elif choice == "2":
#     pass
#   elif choice == "3":
#     pass
#   elif choice == "4":
#     pass
#   elif choice == "5":
#     print("프로그램 종료")
#     break



# for idx,list in enumerate(lists):
#   print(f"{idx+1}. 링크 : https://www.coupang.com"+list.select_one("a")['href'])
#   print(f"2. 상품명 : {list.select_one("div.name").text}")
#   price = list.select_one("strong.price-value")
#   if price == None: continue
#   else:
#     price = int(price.text.replace(",",""))
#   print(f"3. 가격 : {price:,}원")
#   rating = list.select_one("em.rating")
#   if rating == None: continue
#   else:
#     rating = float(rating.text)
#   print(f"4. 평점 : {rating}")
#   num = int(list.select_one("span.rating-total-count").text[1:-1])
#   print(f"5. 평가수 : {num}")
#   print(f"6. 이미지링크 : https:{list.select_one("img")['src']}")
#   print()

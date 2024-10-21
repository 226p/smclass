import requests



# url = [
# "http://www.naver.com",
# "http://www.resom.co.kr/forest/main/main.asp",
# "http://www.coupang.com/"
# ]


# for i in range(len(url)):
#   res = requests.get(url[i],headers=headers)
#   res.raise_for_status()

#   with open(f"c1021/{i}.html","w",encoding="utf-8") as f:
#     f.write(res.text)

# print("프로그램 종료")

url = "http://www.coupang.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()
print(res.text)
# 웹스크래핑 세팅
import requests

# res = requests.get("http://www.google.com")  # html 소스를 가져옴
res = requests.get("http://www.naver.com")  # html 소스를 가져옴
# res = requests.get("https://www.melon.com/index.htm")  # html 소스를 가져옴
res.raise_for_status()  # error시 종료
# print(res.text)  # html소스 출력

# requests로 정보를 가져올 시, 제이쿼리, 자바스크립트, 외부페이지, react, vue .. 비동기식으로 작동되는 소스는 가져오지 못함

print("총 문자 길이 :", len(res.text))

# f = open("a.html","w",encoding="utf-8")
# f.write(res.txt)
# f.close()

# f.close() 안해도 자동으로 닫히는 문법
with open("c1021/b.html","w",encoding="utf-8") as f:   # 웹소스코드 파일 저장
  f.write(res.text)



print("응답코드 :",res.status_code)   # 200(서버가 성공적으로 처리할 시)

# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근할 수 없습니다.")


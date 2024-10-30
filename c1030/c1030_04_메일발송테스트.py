import oracledb
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# 이메일로 임시 비밀번호 전송
smtpName = "smtp.naver.com"
smtpPort = 587

# id, pw, 받는사람이메일주소
sendEmail = "qkrdnwjd0893@naver.com"
pw1 = "7VZNPVDYKYRK"
recvEmail = "qkrdnwjd0893@naver.com"

title = "제목 : 커뮤니티 임시 비밀번호 발급 안내"
content = "◟(ᵔ ̮ ᵔ)͜   ♡ 당신의 임시 비밀번호 : 1234"

# 설정
msg = MIMEText(content)
msg['Subject'] = title
msg["From"] = sendEmail
msg['To'] = recvEmail
print("msg 데이터 : ",msg.as_string())

# 서버이름,서버포트
s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()  # 보안연결
s.login(sendEmail,pw1)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.quit()
# 메일발송 완료
print("임시비밀번호를 가입한 메일로 발송하였습니다. 다시 로그인하세요.")
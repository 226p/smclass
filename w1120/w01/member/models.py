from django.db import models
import datetime

class Member(models.Model):
  id = models.CharField(max_length=50,primary_key=True) # Null, 중복 안됨
  pw = models.CharField(max_length=100,blank=False)      # 빈칸 안됨(데이터 들어와야 함)
  name = models.CharField(max_length=100)
  nickname = models.CharField(max_length=100)
  cdate = models.DateTimeField(auto_now=True)  # 자동으로 현재시간 입력
  # cdate = models.DateTimeField(default=datetime.datetime.now())

  def __str__(self):
    return f"{self.id},{self.name}"

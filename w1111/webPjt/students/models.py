from django.db import models

# Create your models here.
## 오라클에서 table생성가능, insert, update, select, delete
## orm : 오라클 접속하지 않고 table 생성가능
class Student(models.Model):
  s_name = models.CharField(max_length=100)
  s_major = models.CharField(max_length=100)
  s_age = models.IntegerField(default=0)
  s_grade = models.IntegerField(default=0)
  s_gender = models.CharField(max_length=30)

  def __str__(self):
    return self.s_name
from django.contrib import admin
from students.models import Student

# 관리자페이지에서 3개의 카테고리로 보여줌
class StudentAdmin(admin.ModelAdmin):
  list_display = ['name','major','grade','age','gender']

admin.site.register(Student,StudentAdmin)
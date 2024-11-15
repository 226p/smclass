from django.contrib import admin
from students.models import Students

### admin관리자페이지에서 컬럼 보여지는 부분설정
class StudentAdmin(admin.ModelAdmin):
  list_display = ['s_name','s_major','s_grade','s_age']

### admin페이지에 추가
admin.site.register(Students,StudentAdmin)
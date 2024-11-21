from django.contrib import admin
from member.models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id','name','nickname','mdate']

# 관리자페이지 컬럼
# admin.site.register(Member,MemberAdmin)
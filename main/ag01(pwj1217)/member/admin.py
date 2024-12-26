from django.contrib import admin
from member.models import Member,Star,Reservation,delMember,Rating

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'nickname', 'mDate']

@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ("sNo", "member", "fboard", "sDate")


@admin.register(Reservation)
class ResAdmin(admin.ModelAdmin):
  list_display = ['rNo','resPeople','resMemo','rDate']

@admin.register(delMember)
class delMemberAdmin(admin.ModelAdmin):
  list_display = ['dNo','id','dDate']

@admin.register(Rating)
class RationgAdmin(admin.ModelAdmin):
    list_display = ['rNo','member','food','cafe','rating','rDate']
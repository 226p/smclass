from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from member.models import Member
from django.core import serializers # json타입


def login(request):   # 로그인페이지 호출
  return render(request,'login.html')

def loginChk(request):   # 로그인 체크
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  qs = Member.objects.filter(id=id,pw=pw)
  print(id,pw)
  if qs:
    request.session['session_id'] = qs[0].id
    request.session['session_nicName'] = qs[0].nicName
    list_qs = list(qs.values())
    context = {"result":"success","member":list_qs}
  else:
    context = {"result":"fail"}

  return JsonResponse(context)

def logout(request):
  request.session.clear()
  return redirect("/")
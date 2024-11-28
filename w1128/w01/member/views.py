from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from member.models import Member
from django.core import serializers # json타입

def login(request):   # 로그인페이지
  return render(request,'login.html')

## json타입 - list, dic타입 / qs:set타입 ->list타입 변경해야 함
# @csrf_exempt  # 예외처리
def loginChk(request):   # 로그인체크
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  print(id,pw)
  # qs = Member.objects.get(id=id,pw=pw)    # 없으면 error
  qs = Member.objects.filter(id=id,pw=pw)    # 없으면 None
  if qs:
    request.session['session_id'] = id
    request.session['session_nickName'] = qs[0].nickName
    qs_list = list(qs.values())
    # json_qs = serializers.serialize('json',[qs])   # get방식
    context = {"result":"success","member":qs_list}
  else:
    print("실패")
    context = {"result":"fail"}
  return JsonResponse(context)

def logout(request):     # 로그아웃
  request.session.clear()
  context = {'outmsg':'1'}
  return render(request,'index.html',context)


def step03(request):    # 회원가입(3)
  return render(request,'step03.html')

def idChk(request):
  id = request.POST.get("id","")
  print(id)
  qs = Member.objects.filter(id=id)
  if not qs:
    context = {"result":"success"}
  else:
    qs_list = list(qs.values())
    context = {"result":"fail","member":qs_list}
  return JsonResponse(context)
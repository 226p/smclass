from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from member.models import Member
from django.core import serializers   # json타입으로 변경

def login(request):   # 로그인페이지 호출
  return render(request, 'login.html')

# @csrf_exempt  #crsf_token 예외처리
def loginChk(request): # ajax통신
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  print("html에서 넘어온 데이터 :",id,pw)
  ## get 검색 객체 보내는 방법
  # qs = Member.objects.get(id=id,pw=pw)
  # json_qs = serializers.serialize('json',qs)
  # if qs:
  #   context = {"member":json_qs, "result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)

  # 객체 보내는 방법(qs를 리스트로 바꿔줘야 함 : TypeError발생)
  qs = Member.objects.filter(id=id,pw=pw)
  mlist = list(qs.values())
  # qs = list(Member.objects.filter(id=id,pw=pw).values()) 
  if qs:
    context = {"member":mlist, "result":"success"}
  else:
    context = {"result":"fail"}
  return JsonResponse(context)

  # 변수 보내는 방법
  # if qs:
  #   context = {"id":qs[0].id,"nickName":qs[0].nickName, "result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)

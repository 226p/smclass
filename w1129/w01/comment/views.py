from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from member.models import Member
from board.models import Board
from comment.models import Comment
from django.core import serializers # json타입

def cwrite(request):   # 하단댓글 저장
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  board = Board.objects.get(bno=bno)
  cpw = request.POST.get("cpw","")
  ccontent = request.POST.get("ccontent","")

  print(cpw,ccontent)
  qs = Comment.objects.create(member=member,board=board,cpw=cpw,ccontent=ccontent)
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print("확인:",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)

def cdelete(request):   # 하단댓글 삭제
  cno = request.POST.get("cno")
  print(cno)
  Comment.objects.get(cno=cno).delete()

  context = {"result":"success"}
  return JsonResponse(context)

def cupdate(request):   # 하단댓글 수정저장
  id = request.session['session_id']
  cno = request.POST.get("cno")
  ccontent = request.POST.get("ccontent")

  print(cno,ccontent)
  qs = Comment.objects.get(cno=cno)
  qs.ccontent = ccontent
  qs.save()
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print("확인:",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)
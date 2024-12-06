from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from django.db.models import Q
from django.db.models import F
from comment.models import Comment
from member.models import Member
from board.models import Board


def cwrite(request):    ## 하단댓글 저장
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  print(bno)
  board = Board.objects.get(bno=bno)
  ccontent = request.POST.get("ccontent","")
  print("cwrite 확인: ", bno, ccontent)
  
  qs = Comment.objects.create(member=member,board=board,ccontent=ccontent)
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print("cwrite qs확인 : ",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)

def reply(request):
  cno = request.POST.get("cno")
  bno = request.POST.get("bno")
  ccontent = request.POST.get("ccontent")

  print(cno,bno,ccontent)
  id = request.session.get('session_id')
  member = Member.objects.get(id=id)
  board = Board.objects.get(bno=bno)
  cgroup = int(request.POST.get("cgroup"))
  cstep = int(request.POST.get("cstep"))
  cindent = int(request.POST.get("cindent"))
  qs = Comment.objects.filter(cgroup=cgroup,cstep__gt=cstep)
  qs.update(cstep=F('cstep')+1)

  Comment.objects.create(member=member,board=board,ccontent=ccontent,\
                        cgroup=cgroup+1,cstep=cstep+1,bindent=cindent+1)

  context = {'rmsg':cno}

  return JsonResponse(context)

def cdelete(request):    ## 하단댓글 삭제
  cno = request.POST.get("cno")
  print("확인 : ",cno)
  Comment.objects.get(cno=cno).delete()
  context = {"result":"success"}
  return JsonResponse(context)


def cupdate(request):    ## 하단댓글 수정저장
  id = request.session['session_id']
  cno = request.POST.get("cno")
  ccontent = request.POST.get('ccontent')
  print("확인 : ",cno,ccontent)
  # 수정
  qs = Comment.objects.get(cno=cno)
  qs.ccontent = ccontent
  qs.save()
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print("qs확인 : ",list_qs)
  context = {"result":"success","comment":list_qs}
  return JsonResponse(context)
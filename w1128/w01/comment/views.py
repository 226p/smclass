from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from member.models import Member
from board.models import Board
from django.core import serializers # json타입
from comment.models import Comment

def clist(request):    # 하단 댓글 리스트
  return

def cwrite(request):    # 하단 댓글 작성
  ## 데이터 가져오기
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  board = Board.objects.get(bno=bno)
  ccontent = request.POST.get("ccontent")
  cpw = request.POST.get("pw","")
  print(cpw,ccontent)

  # 데이터 저장
  qs = Comment.objects.create(board=board,member=member,cpw=cpw,ccontent=ccontent)
  json_qs = serializers.serialize("json",[qs])
  context = {"comment":json_qs,"result":"success"}
  return JsonResponse(context)
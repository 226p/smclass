from django.shortcuts import render
from board.models import Board
from comment.models import Comment

def blist(request):    # 게시판리스트
  qs = Board.objects.all().order_by('-bgroup','bstep')
  context = {'blist':qs}
  return render(request,'blist.html',context)

def bview(request,bno):    # 게시판 상세보기
  qs = Board.objects.filter(bno=bno)
  board = Board.objects.get(bno=bno)
  c_qs = Comment.objects.filter(board=board)
  context = {'board':qs[0],'comment':c_qs}
  return render(request,'bview.html',context)
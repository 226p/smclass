from django.shortcuts import render
from board.models import Board
from comment.models import Comment
from member.models import Member
from django.http import JsonResponse,HttpResponse

## form
def form(request):
  if request.method == "GET":
    return render(request,'form.html')
  else:
    file1 = request.FILES.get('bfile')
    print("file1 : ",file1)
    file_list = request.FILES.getlist('bfile')
    print("파일 : ",file_list)
    return HttpResponse(file_list) 


## 상세보기
def bview(request,bno):
  id = request.session["session_id"]
  member = Member.objects.get(id=id)
  qs = Board.objects.filter(bno=bno)
  if qs[0].like_member.filter(pk=id).exists():
    ## 좋아요 클릭했을 때,
    result = "1"  # 좋아요 있으면
  else:
    result = "0"  # 좋아요 없으면
  count = qs[0].like_member.count()

  # 하단댓글가져오기
  c_qs = Comment.objects.filter(board=qs[0]).order_by("-cno")
  print("확인 : ",c_qs,c_qs.count)
  context = {"board":qs[0],"clist":c_qs,"result":result,"count":count}
  return render(request,'bview.html',context)


## 게시판리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)

## 좋아요 / board, member
def likes(request):
  id = request.session["session_id"]
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno")
  board = Board.objects.get(bno=bno)

  if board.like_member.filter(pk=id).exists():
    ## 좋아요 클릭했을 때,
    board.like_member.remove(member)
    result = "remove"  # 좋아요 삭제
  else:
    board.like_member.add(member)
    result = "add"  # 좋아요 추가
  print("좋아요 갯수 확인",board.like_member.count())
  context = {"result":result,"count":board.like_member.count()}
  return JsonResponse(context)
from django.shortcuts import render
from board.models import Board
from member.models import Member
from django.db.models import Q
from django.db.models import F
from datetime import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse 
from comment.models import Comment

def nboard(request):    # 1. 게시판리스트 호출(bselect태그에 따른 호출) / 2. 게시판 하단 넘버링
  if request.method == 'GET':
    bselect = request.GET.get("bselect","전체")
    print("bselect : ",bselect)
    if bselect == "전체":
      qs = Board.objects.all().order_by("-bgroup","bstep")
      print("qs : ",qs)
    elif bselect == "인기글":
      qs = Board.objects.all().order_by("-like_member")
      print("qs : ",qs)
    else:
      qs = Board.objects.filter(bselect=bselect).order_by("-bgroup","bstep")
      print("qs : ",qs)

    npage = int(request.GET.get('npage',1))
    print("npage:",npage)
    paginator = Paginator(qs,10)
    blist = paginator.get_page(npage)

    # 각 게시글에 대한 댓글 수를 계산하여 전달
    comment_counts = {board.bno: Comment.objects.filter(board=board).count() for board in blist}
    context = {"blist": blist, 'npage': npage, 'comment_counts': comment_counts}
    return render(request,'nboard.html',context)
  else:
    return render(request,'nboard.html')

def bwrite(request):    # 1. 게시판글작성 호출 / 2. 게시판 글 작성 저장
  if request.method == 'GET':
    return render(request, 'bwrite.html')
  else:
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)

    btitle = request.POST.get('btitle')
    bselect = request.POST.get('bselect')
    bcontent = request.POST.get('bcontent')
    bgps = request.POST.get('bgps')
    bfile = request.FILES.get("bfile","")

    qs = Board.objects.create(member=member,btitle=btitle,bselect=bselect,bcontent=bcontent,bgps=bgps,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    context = {'wmsg':'1'}
    return render(request,'bwrite.html',context)

def gps_test(request):    # gps테스트 호출(테스트)
  return render(request, 'gps_test.html')

def bbview(request,bno):    # 1. 게시글 상세보기 / 2. 좋아요 클릭 / 3. 이전글, 다음글 / 4. 댓글 리스트 출력 / 5. 조회수 늘리는 방법
  id = request.session["session_id"]
  member = Member.objects.get(id=id)
  
  qs__ = Board.objects.filter(bno=bno)
  if qs__[0].like_member.filter(pk=id).exists():
    result = "1"  # 좋아요 있으면
  else:
    result = "0"  # 좋아요 없으면
  count = qs__[0].like_member.count()
  print(count)
  npage = request.GET.get('npage',1)

  qs = Board.objects.get(bno=bno)

  next_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep)|Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by('-bgroup','bstep').first()
  prev_qs = Board.objects.filter(Q(bgroup__gt=qs.bgroup,bstep__gte=qs.bstep)|Q(bgroup=qs.bgroup,bstep__lt=qs.bstep)).order_by('bgroup','-bstep').first()
  
  c_qs = Comment.objects.filter(board=qs).order_by("-cno")
  print("확인 : ",c_qs,c_qs.count)
  
  day1 = datetime.replace(datetime.now(),hour=23,minute=59,second=59)
  expires = datetime.strftime(day1,"%a, %d-%b-%Y %H:%M:%S GMT")
  context = {'board':qs,'prev_qs':prev_qs,'next_qs':next_qs,"result":result,"count":count,"clist":c_qs}
  response = render(request,'bbview.html',context)

  if request.COOKIES.get("cookie_boardNo") is not None:
    cookies = request.COOKIES.get("cookie_boardNo")
    cookies_list = cookies.split("|")
    if str(bno) not in cookies_list:
      ## 쿠키저장
      response.set_cookie("cookie_boardNo",cookies+f"|{bno}",expires=expires)
      ## 조회수 1증가
      qs.bhit += 1
      qs.save()
  else:  ## 쿠키저장
    response.set_cookie('cookie_boardNo',bno,expires=expires)
    ## 조회수 1증가
    qs.bhit += 1
    qs.save()
  return response 

def bdelete(request,bno):    # 글 삭제하기
  Board.objects.get(bno=bno).delete()
  context = {"dmsg":bno}
  return render(request,'nboard.html',context)

def bmodify(request,bno):   # 1. 글수정페이지 호출 / 2. 글수정 저장
  if request.method == 'GET':
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,'bmodify.html',context)
  else:
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bgps = request.POST.get("bgps")
    bselect = request.POST.get("bselect")
    bfile = request.FILES.get("bfile","")   # file 안 넣으면 빈 공백
    print("파일정보 :",bfile)

    ## 게시글 수정 저장 / 입력해야하는 것 : member, btitle, bcontent, bgps, bselect, bfile
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.bgps = bgps
    qs.bselect = bselect
    if bfile: qs.bfile = bfile
    qs.save()

    context = {'umsg':bno}
    return render(request,'bmodify.html',context)
  
def likes(request):   # 좋아요 숫자증가
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
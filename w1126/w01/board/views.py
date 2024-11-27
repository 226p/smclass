from django.shortcuts import render
from board.models import Board
from member.models import Member
from datetime import datetime
from django.db.models import Q
from django.db.models import F
from django.core.paginator import Paginator

def blist(request):   # 게시판페이지 호출
  npage = int(request.GET.get('npage',1))  # 넘어온 현재페이지
  qs = Board.objects.all().order_by('-bgroup','bstep')
  ## 하단 페이지 넘버링
  paginator = Paginator(qs,10)  # 중간에 삭제해도 알아서 계산해줌 / 1페이지 10개
  blist = paginator.get_page(npage)

  context = {'blist':blist,'npage':npage}

  return render(request,'blist.html',context)

def bwrite(request):   # 1. 글쓰기페이지 호출 / 2. 글쓰기 저장
  if request.method == 'GET':
    return render(request,'bwrite.html')
  else:
    id = request.session.get('session_id')
    # id = request.session['session_id']
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")   # file 안 넣으면 빈 공백
    print("파일정보 :",bfile)

    ## 게시글 저장 / 입력해야하는 것 : member, btitle, bcontent, bfile
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    context = {'wmsg':'1'}
    return render(request,'bwrite.html',context)

def bview(request,bno):   # 1. 글 상세보기 / 2. 조회수 증가 / 3. 이전글, 다음글
  npage = request.GET.get('npage',1)
  qs = Board.objects.get(bno=bno)

  ### 이전글, 다음글 (Q함수 사용)
  prev_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep)|Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by('-bgroup','bstep').first()
  next_qs = Board.objects.filter().order_by('-bgroup','bstep').first()

  ### 조회수 증가 방지
  ## 날짜 지정 / 쿠키사용
  day1 = datetime.replace(datetime.now(),hour=23,minute=59,second=59)
  expires = datetime.strftime(day1,"%a, %d-%b-%Y %H:%M:%S GMT")  # 포멧시간 지정
  context = {"board":qs,"prev_board":prev_qs,"next_board":next_qs,"npage":npage}
  response =  render(request,'bview.html',context)
  print(expires)
  ## 쿠키확인
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
  
def bdelete(request,bno):   # 글 삭제
  Board.objects.get(bno=bno).delete()
  context = {"dmsg":bno}
  return render(request,'blist.html',context)
  
def bupdate(request,bno):   # 1. 글수정페이지 호출 / 2. 글수정 저장
  if request.method == 'GET':
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,'bupdate.html',context)
  else:
    bno = request.POST.get("bno")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")   # file 안 넣으면 빈 공백
    print("파일정보 :",bfile)

    ## 게시글 수정 저장 / 입력해야하는 것 : member, btitle, bcontent, bfile
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    if bfile: qs.bfile = bfile
    qs.save()

    context = {'umsg':bno}
    return render(request,'bupdate.html',context)
  
def breply(request,bno):   # 1. 답글페이지 호출 / 2. 답글 저장
  if request.method == 'GET':
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,'breply.html',context)
  else:
    bno = request.POST.get("bno")
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    bgroup = int(request.POST.get("bgroup"))
    bstep = int(request.POST.get("bstep"))
    bindent = int(request.POST.get("bindent"))
    qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
    qs.update(bstep=F('bstep')+1)

    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")   

    Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile,\
                         bgroup=bgroup,bstep=bstep+1,bindent=bindent+1)

    context = {'rmsg':bno}
    return render(request,'breply.html',context)
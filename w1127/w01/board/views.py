from django.shortcuts import render
from board.models import Board
from member.models import Member
from django.db.models import Q
from django.db.models import F
from datetime import datetime

def blist(request):   # 게시판 호출
  if request.method == 'GET':
    qs = Board.objects.all().order_by('-bgroup','bstep')
    context = {'blist':qs}
    return render(request,'blist.html',context)
  
def bwrite(request):   # 1. 게시판 글쓰기 / 2. 글 저장
  if request.method == 'GET':
    return render(request,'bwrite.html')
  else:
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get("bfile","")
    print("파일정보 :",bfile)

    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    context = {'wmsg':'1'}
    return render(request,'bwrite.html',context)
  
def bview(request,bno):   # 1. 글 상세보기 / 2. 조회수 증가 / 3. 이전글, 다음글
  qs = Board.objects.get(bno=bno)

  prev_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep)|Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by('-bgroup','bstep').first()
  next_qs = Board.objects.filter(Q(bgroup__gt=qs.bgroup,bstep__gte=qs.bstep)|Q(bgroup=qs.bgroup,bstep__lt=qs.bstep)).order_by('bgroup','-bstep').first()

  day1 = datetime.replace(datetime.now(),hour=23,minute=59,second=59)
  expires = datetime.strftime(day1,"%a, %d-%b-%Y %H:%M:%S GMT")
  context = {'board':qs,'prev_qs':prev_qs,'next_qs':next_qs}
  response = render(request,'bview.html',context)

  if request.COOKIES.get("cookie_boardNo") is not None:
    cookies = request.COOKIES.get("cookie_boardNo")
    cookies_list = cookies.split("|")
    if str(bno) not in cookies_list:
      response.set_cookie("cookie_boardNo",cookies+f"|{bno}",expires=expires)
      qs.bhit += 1
      qs.save()
  else:
    response.set_cookie("cookie_boardNo",bno,expires=expires)
    qs.bhit += 1
    qs.save()
  return response


from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member
from django.db.models import F
from datetime import datetime

def blist(request):   # 게시판리스트 호출
  qs = Board.objects.all().order_by('-bgroup','bstep')
  context = {'blist':qs}
  return render(request,'blist.html',context)

def bwrite(request):   # 1. 글쓰기페이지 호출, 2. 글쓰기 저장
  if request.method == 'GET':
    return render(request,'bwrite.html')
  else: 
    id = request.session.get('session_id')  # session_id 갖고옴
    member = Member.objects.get(id=id)
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bimg = request.FILES.get('bimg','')
    print(bimg)

    ## DB저장 - AutoField : 번호생성
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bimg=bimg)
    qs.bgroup = qs.bno
    qs.save()

    context = {'wmsg':'1'}
    return render(request,'bwrite.html',context)
  
def bview(request,bno):  # 글 상세보기(조회수, 이전글, 다음글)
  ## 쿠키 사용기간 - 1일동안 유지 (11월25일 23시59분0초)
  tomorrow = datetime.replace(datetime.now(),hour=23,minute=59,second=0)
  ## 쿠키설정포맷 - strftime: 시간포맷 
  expires = datetime.strftime(tomorrow,"%a,%d-%b-%Y %H:%M:%S GMT")
  ## get()
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save()

  qs = Board.objects.filter(bno=bno)
  ## 이전글, 다음글 가져오기
  prev_qs = Board.objects.filter().order_by('-bgroup','bstep').first()
  next_qs = Board.objects.filter().order_by('bgroup','bstep').first()
  context = {'board':qs[0]}
  response = render(request,'bview.html',context)
  ## filter() - update()
  ## F 함수 - 필드 값을 참조
  print("cookies_name :",request.COOKIES.get('cookie_name'))
  ## 조회수↑ cookie_name 증가한 번호추가
  if request.COOKIES.get('cookie_name') is not None:  # cookie_name 존재하면
    # 쿠키가 존재하면 쿠키 읽어와서 1|3|4 -> 2:1증가 3:증가안됨
    cookies = request.COOKIES.get('cookie_name')
    cookies_list = cookies.split("|")   # 번호없으면 번호 추가 
    if str(bno) not in cookies_list:
      print('cookie_name 있지만, 번호가 없으면')
      response.set_cookie('cookie_name',cookies+f'|{bno}',expires=expires)
      qs.update(bhit = F('bhit')+1)

  else:  # cookie_name 존재하지 않으면 : 처음으로 게시글 조회
    print('cookie_name 없으면')
    response.set_cookie('cookie_name',bno,expires=expires)
    qs.update(bhit = F('bhit')+1)
  
  return response

def bdelete(request,bno):  # 글 삭제
  qs = Board.objects.get(bno=bno)
  qs.delete()
  context = {'dmsg':bno}
  return render(request,'blist.html',context)

def bupdate(request,bno):  # 1. 글 수정 / 2. 수정한 글 저장
  if request.method == 'GET':
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'bupdate.html',context)
  else:
    bno = request.POST.get('bno')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()

    return redirect('board:bview',bno)
  
def breply(request,bno):
  if request.method == 'GET':
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'breply.html',context)
  else:
    id = request.POST.get('id')
    member = Member.objects.get(id=id)
    bgroup = int(request.POST.get('bgroup'))   # 답글 그룹핑
    bstep = int(request.POST.get('bstep'))   # 답글 순서
    bindent = int(request.POST.get('bindent'))   # 들여쓰기
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')

    ## 같은 bgroup에서 bstep이 더 큰 것만 검색 후, 데이터 1씩 증가
    qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
    qs.update(bstep=F('bstep')+1)

    qs = Board(member=member,btitle=btitle,bcontent=bcontent,\
               bgroup=bgroup,bstep=bstep+1,bindent=bindent+1)
    qs.save()
    context = {'rmsg':'1'}
    return render(request, 'breply.html',context)

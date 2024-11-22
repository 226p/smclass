from django.shortcuts import render, redirect
from board.models import Board
from django.contrib import messages
from django.db.models import F

def blist(request):  # 게시판리스트
  qs = Board.objects.all().order_by('-bgroup','bstep')
  context = {"blist":qs}
  return render(request, 'blist.html',context)

def bwrite(request):  # 게시판 글쓰기 페이지 호출, 글쓰기 저장
  if request.method == 'GET':
    return render(request, 'bwrite.html')
  else :
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    # bno,bdate 자동 / id,btitle,bcontent,bgroup - 입력 / bstep,bindent,bhit - 0
    ## DB저장
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    # messages.success(request, message='게시글이 저장되었습니다.')

    return render(request, 'bwrite.html',{'msg':'1'})
    # return redirect('board:blist')

def bview(request, bno):  # 글 상세보기
  print('게시글 번호 :',bno)
  ## 조회수 1씩 증가
  # get 쓰는 방법
  qs = Board.objects.get(bno=bno)
  qs.bhit += 1
  qs.save()

  # filer 쓰는 방법 / F함수 : filter로 검색된 값으로 호출
  # qs = Board.objects.filter(bno=bno)
  # qs.update(bhit=F('bhit')+1)
  # context = {'board':qs[0]}

  context = {'board':qs}
  return render(request,'bview.html',context)

def bmodify(request, bno):  # 1. 글 수정 페이지 호출 / 2. 글 수정 저장
  if request.method == 'GET':
    qs = Board.objects.filter(bno=bno)
    context = {"board":qs[0]}
    return render(request,'bmodify.html',context)
  else :
    bno = request.POST.get('bno')
    print(bno)
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()

    return render(request, 'bmodify.html',{'u_msg':bno})
    # return redirect('board:bview')

def bdelete(request,bno):  # 글 삭제하기
  print('게시글 번호 :',bno)
  Board.objects.get(bno=bno).delete()
  return render(request,'blist.html',{"d_msg":bno})

def breply(request,bno):  # 글 답변달기
  if request.method == 'GET':
    print('게시글 번호 :',bno)
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'breply.html',context)
  else:
    bgroup = int(request.POST.get('bgroup'))   # str타입>int타입
    bstep = int(request.POST.get('bstep'))
    bindent = int(request.POST.get('bindent'))
    btitle = request.POST.get('btitle')
    id = request.POST.get('id')
    bcontent = request.POST.get('bcontent')
    print('bgroup 번호 :',bgroup)

    ## 다른 답변달기에 bstep 1씩 증가
    qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
    qs.update(bstep = F('bstep')+1)

    # bgroup : 부모의 bgroup 입력
    Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bgroup=bgroup\
                         ,bstep=bstep+1,bindent=bindent+1)
    
    # return redirect('board:blist')
    return render(request,'blist.html',{'r_msg':'1'})

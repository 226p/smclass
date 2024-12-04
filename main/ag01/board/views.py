from django.shortcuts import render
from board.models import Board
from member.models import Member
from django.db.models import Q
from django.db.models import F
from datetime import datetime
from django.core.paginator import Paginator

def nboard(request):    # 1. 게시판리스트 호출(bselect태그에 따른 호출) / 2. 게시판 다음장 넘기기
  if request.method == 'GET':
    bselect = request.GET.get("bselect","전체")
    print("bselect : ",bselect)
    if bselect == "전체":
      qs = Board.objects.all().order_by("-bgroup","bstep")
      print("qs : ",qs)
    else:
      qs = Board.objects.filter(bselect=bselect).order_by("-bgroup","bstep")
      print("qs : ",qs)

    npage = int(request.GET.get('npage',1))
    print("npage:",npage)
    paginator = Paginator(qs,10)
    blist = paginator.get_page(npage)

    context = {"blist":blist,'npage':npage}
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

def gps_test(request):    # gps테스트 호출
  return render(request, 'gps_test.html')


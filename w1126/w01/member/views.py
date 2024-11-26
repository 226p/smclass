from django.shortcuts import render
from member.models import Member

def login(request):   # 1. 로그인페이지 호출 / 2. 로그인
  if request.method == 'GET':
    return render(request,'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)

    if qs:
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName

      context = {'lmsg':'1'}
    else:
      context = {'lmsg':'0'}
    return render(request,'login.html',context)

def logout(request):   # 로그아웃
  request.session.clear()  # 모든 세션 삭제 / del request.session['session_id'] 1개삭제
  context = {'lmsg':'1'}
  return render(request,'index.html',context)
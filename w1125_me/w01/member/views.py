from django.shortcuts import render, redirect
from member.models import Member

def login(request):   # 1. 로그인페이지 호출 / 2. 로그인 확인
  if request.method == 'GET':
    return render(request,'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)
    
    if qs:  ## member 있을 경우
      request.session['session_id'] = qs[0].id
      request.session['session_nickName'] = qs[0].nickName
      context = {'lmsg':'1'}
    else:  ## member 없을 경우
      context = {'lmsg':'0'}
    return render(request,'login.html',context)
  
def logout(request):   # 로그인아웃
  request.session.clear()
  return redirect('/')
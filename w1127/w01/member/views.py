from django.shortcuts import render
from member.models import Member

def login(request):
  if request.method == 'GET':
    return render(request,'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      request.session['session_id'] = id
      request.session['session_nickName'] = qs[0].nickName

      context = {'lmsg':'1'}
    else:
      context = {'lmsg':'0'}
    return render(request,'login.html',context)

def logout(request):
  request.session.clear()
  context = {'lmsg':'1'}
  return render(request,'index.html',context)
from django.shortcuts import render,redirect
from member.models import Member

def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      msg = "로그인 성공"
      print(msg)
      request.session['session_id'] = id
      request.session['session_name'] = qs[0].name
      return redirect('index')    # msg가 안 넘어감
    else: 
      msg = "아이디 또는 패스워드가 일치하지 않습니다."
    return render(request,'login.html',{"msg":msg})

def logout(request):
  request.session.clear()
  return redirect('/')

def join01(request):
  return render(request,'join01.html')
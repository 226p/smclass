from django.shortcuts import render, redirect
from member.models import Member

def login(request):   # 1. 로그인페이지 호출(GET) / 2. 로그인 버튼 클릭시(POST)
  if request.method == 'GET':
    return render(request,'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      msg = '로그인 성공'
      print(msg)
      ## 세션연결
      request.session['session_id'] = id
      request.session['session_nickname'] = qs[0].nickname
      return redirect('index')
    else:
      msg = "아이디 또는 패스워드가 일치하지 않습니다."
    return render(request,'login.html',{"login_msg":msg})
  

def logout(request):   # 로그아웃
  request.session.clear()
  ## del request.session['session_id]
  return redirect("/")

def mlist(request):   # 회원리스트 
  id = request.session['session_id']
  if id == 'admin':
    qs = Member.objects.all()
    context = {"mlist":qs}  
  else:
    qs = Member.objects.filter(id=id)
    context = {"mlist":qs}  
  return render(request, 'mlist.html',context)

def mview(request,id):   # 회원상세보기
  print("아이디 정보 :", id)
  qs = Member.objects.filter(id=id)
  print(qs)
  if qs: context = {'mem':qs[0]}

  return render(request,'mview.html',context)

def mwrite(request):   # 회원가입
  if request.method =='GET':
    return render(request,'mwrite.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    name = request.POST.get("name")
    nickname = request.POST.get("nickname")
    tel = request.POST.get("tel")
    gender = request.POST.get("gender")
    hobbys = request.POST.getlist("hobby")
    hobby = ','.join(hobbys)
    Member.objects.create(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)
    # qs = Member(id=id,pw=pw,name=name,nickname=nickname,tel=tel,gender=gender,hobby=hobby)
    # qs.save()
    return redirect("member:mlist")

def mupdate(request,id):   # 회원정보 수정
  if request.method == 'GET':
    print("아이디 정보 :", id)
    qs = Member.objects.filter(id=id)
    context = {"mem":qs[0]}
    return render(request,'mupdate.html',context)
  else: 
    print(id)
    id = request.session['session_id'] # 관리자가 아니면, 세션을 가지고 저장
    ## 관리자 로그인이면, id가져와서 저장
    if request.session['session_id'] == 'admin':
      id = request.POST.get("id")
    pw = request.POST.get("pw")
    name = request.POST.get("name")
    nickname = request.POST.get("nickname")
    tel = request.POST.get("tel")
    gender = request.POST.get("gender")
    hobbys = request.POST.getlist("hobby")
    hobby = ','.join(hobbys)
    qs = Member.objects.get(id=id)

    qs.pw = pw
    qs.name = name
    qs.nickname = nickname
    qs.tel = tel
    qs.gender = gender
    qs.hobby = hobby
    qs.save()

    return redirect('member:mlist')
  

def mdelete(request,id):   # 회원정보 삭제
  Member.objects.get(id=id).delete()
  return redirect(request,"member:mlist")
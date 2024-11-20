from django.shortcuts import render
from member.models import Member

def mlist(request):   # 학생전체리스트 페이지 호출
  qs = Member.objects.all()
  context = {"mlist":qs}
  return render(request,'mlist.html',context)

def login(request):   # 로그인 페이지 호출
  if request.method == 'GET':    # 기본으로 들어가면 GET
    ## 쿠키 검색(user.PC에 쿠키 정보를 포함하고 있음(request))
    print("쿠키정보 :", request.COOKIES)
    print("cookinfo 쿠키정보 :", request.COOKIES.get('cookinfo'))
    #----- 추가 설정
    saveId = request.COOKIES.get('saveId','')
    print(saveId)
    context = {'saveId':saveId}
    ## 쿠키 설정(저장)
    response = render(request,'login.html',context)

    # render(request,'login.html').set_cookie('cookinfo','1111')

    ## 쿠키 정보 검색
    if request.COOKIES.get('cookinfo'): 
      response.set_cookie('cookinfo','1111',max_age=60*60)  # 기본은 브라우저 종료 시 삭제(세션만료까지) / max_age=60초*60분으로 설정 / 한달은 60*60*24*30

    return response
  else:    # submit버튼 누르면 POST
    print("쿠키정보 :", request.COOKIES)
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    saveId = request.POST.get("saveId")
    print("전달받은 정보 :",id, pw, saveId)

    response = render(request,'login.html')
    ## 아이디 기억하기 정보가 있다면
    if saveId is not None :   # 아이디 기억하기 체크 있으면, 쿠키저장
      response.set_cookie('saveId',id,max_age=60*60)
    else : response.delete_cookie('saveId')   # 아이디 기억하기 체크 없을 때, 쿠키삭제
    return response
  
def login2(request):
  if request.method == 'GET':
    cookId = request.COOKIES.get('cookId','')
    print(cookId)
    context = {"cookId":cookId}
    return render(request,'login2.html',context)
    
  else:
    response = render(request,'index.html')
    ## 3개 정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')

    if saveId is not None:   # savId 체크되면 아이디 쿠키저장, 아니면 쿠키삭제
      response.set_cookie('cookId',id,max_age=60*60)
    else: response.delete_cookie('cookId')
    return response
  
def product(request):
  if request.method == 'GET':   # 쿠키 읽어오기
    c_pId = request.COOKIES.get('c_pId','')
    c_pName = request.COOKIES.get('c_pName','')
    context = {'c_pId':c_pId,'c_pName':c_pName}
    response = render(request,'product.html',context)
    return response
  else:   # 쿠키 저장하기
    response = render(request,'index.html')
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    option = request.POST.get('option')
    saveP = request.POST.get('saveP')
    print(pId, pName, option, saveP)

    if saveP is not None:    # saveP 체크되어 있으면 쿠키생성
      response.set_cookie('c_pId',pId,max_age=60*60)
      response.set_cookie('c_pName',pName,max_age=60*60)
    else:    # saveP 체크 안되어 있으면 쿠키삭제
      response.delete_cookie('c_pId')
      response.delete_cookie('c_pName')

    return response
  
def m2(request):
  if request.method == 'GET':
    mId = request.COOKIES.get('mId','')
    mPrice = request.COOKIES.get('mPrice','')
    option = request.COOKIES.get('option','')
    context = {'mId':mId,'mPrice':mPrice,'option':option}
    response = render(request, 'm2.html',context)
    return response
  else: 
    response = render(request,'index.html')
    mId = request.POST.get('mId')
    mPrice = request.POST.get('mPrice')
    option = request.POST.get('option')
    saveId = request.POST.get('saveId')
    print(mId,mPrice,option,saveId)

    if saveId is not None:
      response.set_cookie('mId',mId,max_age=60*60)
      response.set_cookie('mPrice',mPrice,max_age=60*60)
      response.set_cookie('option',option,max_age=60*60)
    else :
      response.delete_cookie('mId')
      response.delete_cookie('mPrice')
      response.delete_cookie('option')

    return response
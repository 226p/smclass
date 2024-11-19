from django.shortcuts import render, redirect
from students.models import Student
from django.urls import reverse

def write(request):  # 1. 학생등록페이지 호출 / 2. 학생데이터 입력 후 저장
  if request.method == 'POST':  # form action으로 들어왔을 때 / 2. 학생데이터 입력 후 저장
    name = request.POST.get('name')  # 데이터가 없을 때 None
    major = request.POST.get('major')
    grade = request.POST['grade']    # 데이터가 없을 때 error
    age = request.POST['age'] 
    gender = request.POST['gender']
    # hobby = request.POST['hobby']  /   # checkbox 하나만 넘어옴
    hobbys = request.POST.getlist('hobby')    # checkbox 선택한 것 모두 넘어옴 / 단, 리스트는 저장못함
    hobby = ','.join(hobbys)  # list타입 -> str타입으로 변경 / 저장가능
    # hobby_list = hobby.split(",")  # str타입 -> list타입으로 변경 

    print(name)
    print("hobby :",hobby)
    print("hobbys 복수:",hobbys)

    qs = Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)
    qs.save()
    # create : 별도의 save() 필요없음
    # Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)

    return redirect('/students/list/')
  else :  # 평소에 들어올 때 / 1. 학생등록페이지 호출
  # templates 폴더에서 html 검색
    return render(request,'write.html')


def list(request):  # 학생전체리스트 호출
  qs = Student.objects.order_by('-grade','name')   # order_by 정렬 / 역순은 앞에 -
  # qs = Student.objects.all()
  context = {"slist":qs}
  return render(request,'list.html',context)


def view(request,name):  # 학생정보 상세보기
  qs = Student.objects.get(name=name)
  context = {'stu':qs}
  return render(request,'view.html',context)


def update(request):  # 1. 학생정보 수정 페이지 호출 / 2. 학생정보 수정 후 저장
  if request.method == "GET":
    name = request.GET["name"]
    print(name)
    qs = Student.objects.get(name=name)
    context = {"stu":qs}
    return render(request, 'update.html',context)  # 1. 학생정보 수정 페이지 호출
  else:  # 2. 학생정보 수정 후 저장
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)

    qs = Student.objects.get(name=name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobby
    qs.save()

    return redirect('students:view',name)  # 약식도 가능
    # return redirect(reverse('students:view',args=(name,))) # views/{{stu.name}} 상세보기 페이지에 보내는 것 / 기본형식
  
def delete(request,name):  # 학생정보 삭제
  print("삭제정보 이름 :",name)
  Student.objects.get(name=name).delete()
  return redirect('/students/list/')

def search(request):  # 학생 검색
  search = request.GET.get('search')
  print("검색단어 :",search)
  ## 데이터 검색
  qs = Student.objects.filter(name=search)
  context = {"slist":qs}
  return render(request,'list.html',context)
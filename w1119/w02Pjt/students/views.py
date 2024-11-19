from django.shortcuts import render, redirect
from students.models import Student

def write(request):  # 1. 학생등록페이지 호출 / 2. 학생데이터 입력 후 저장
  if request.method == 'POST':  # form action으로 들어왔을 때 / 2. 학생데이터 입력 후 저장
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    print(name,major,grade,age,gender,hobby)

    qs = Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby)
    qs.save()

    return redirect('/')
  else :
    return render(request,'write.html')  # 평소에 들어올 때 / 1. 학생등록페이지 호출
  
def list(request):  # 학생전체리스트 호출
  qs = Student.objects.all()
  context = {"slist":qs}
  return render(request,'list.html',context)

def view(request,name):
  qs = Student.objects.get(name=name)
  context = {"stu":qs}
  return render(request,'view.html',context)
  
def delete(request,name):
  Student.objects.get(name=name).delete()
  return redirect('/students/list/')

def update(request):
  if request.method == 'GET':
    name = request.GET['name']
    qs = Student.objects.get(name=name)
    context = {"stu":qs}
    return render(request,'update.html',context)
  else : 
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

    return redirect('students:view',name)
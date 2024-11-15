from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

# Create your views here.
def write(request):         # 학생등록페이지 호출
    return render(request,'write.html')

def list(request):         # 학생전체리스트 호출
    return render(request,'stu_list.html')

def save(request):         # 학생정보 입력&저장
  print('학생정보저장 호출')
  if request.method == 'POST' :  # method가 post방식인지 확인
    print('post')
  else : print('get1 :',request.GET)

  if request.GET : print('get2 :',request.GET)  
  if request.POST:  # request.POST 안에 데이터가 있는지
    name = request.POST['s_name']
    major = request.POST['s_major']
    grade = request.POST['s_grade']
    age = request.POST['s_age']
    gender = request.POST['s_gender']
    # print(name,major,grade,age,gender)
    print(age)

    qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    qs.save()
  # return redirect('index')
  return HttpResponseRedirect(reverse('index'))  # reverse : app_name

def list(request):         # 학생전체리스트 호출
  # 학생전체리스트 전달
  qs = Student.objects.all()
  # 정보전달 변수생성
  context = {'list':qs}
  return render(request,'stu_list.html',context)
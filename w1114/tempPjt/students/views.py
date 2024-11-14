from django.shortcuts import render

# Create your views here.
def regStudent(request):
  return render(request,'register.html')   # render : 페이지를 열어줌

from django.shortcuts import render

# Create your views here.
def index(request):
  print('메인화면 호출')
  return render(request,'index.html')
from django.shortcuts import render

def list(request):    # 게시판 호출
  return render(request, 'list.html')
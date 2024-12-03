from django.shortcuts import render

def mview(request):
  return render(request, 'mview.html')

def test(request):
  return render(request, 'test.html')

def test2(request):
  return render(request, 'test2.html')
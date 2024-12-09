from django.shortcuts import render

def mview(request):
  return render(request, 'mview.html')

def test(request):
  return render(request, 'test.html')

def test2(request):
  return render(request, 'test2.html')

def test3(request):
  return render(request, 'test3.html')

def test4(request):
  return render(request, 'test4.html')

def test5(request):
  return render(request, 'test5.html')
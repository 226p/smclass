from django.shortcuts import render

def blist(request):
  return render(request,'blist.html')

def bview(request):
  return render(request, 'bview.html')
from django.shortcuts import render

def nboard(request):
  return render(request,'nboard.html')

def bwrite(request):
  return render(request, 'bwrite.html')
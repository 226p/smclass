from django.shortcuts import render

def mview(request):
  return render(request, 'mview.html')
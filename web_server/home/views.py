from django.shortcuts import render

# Create your views here.

def landing(request, *args, **kwargs):
    return render(request,"home/index.html")
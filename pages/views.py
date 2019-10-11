from django.shortcuts import render
from .models import Train
# Create your views here.
from django.http import HttpResponse
def index(request):
    trains = Train()
    return render(request,'pages/index.html',{'trains':trains})

def about(request):
    return render(request,'pages/about.html')
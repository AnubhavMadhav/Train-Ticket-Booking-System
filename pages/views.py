from django.shortcuts import render
from .models import Train, Ticket, Coach
# Create your views here.
from django.http import HttpResponse


def index(request):
    trains = Train()
    tickets = Ticket()
    coaches = Coach()

    return render(request,'pages/index.html',{'trains':trains , 'tickets':tickets, 'coaches':coaches})

def about(request):
    return render(request,'pages/about.html')
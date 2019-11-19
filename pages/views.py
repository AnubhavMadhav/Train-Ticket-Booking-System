from django.shortcuts import render, get_list_or_404
from .models import Train, Ticket, Coach
# Create your views here.
from django.http import HttpResponse

def details(request):
    source = request.GET['p']
    destination = request.GET['q']
    passengers = request.GET['s']
    try:
        is_return = request.GET['i']
    except:
        is_return = 'No'

    trains = get_list_or_404(Train, source=source, destination=destination)

    return render(request, 'booking/detail.html', {'trains': trains, 'passengers': passengers, 'is_return': is_return})


def index(request):
    #books=Book()
    trains = Train()
    tickets = Ticket()
    coaches = Coach()

   # return render(request,'pages/index.html',{'books':books})

    return render(request,'pages/index.html',{'trains':trains , 'tickets':tickets, 'coaches':coaches})


def about(request):
    return render(request,'pages/about.html')
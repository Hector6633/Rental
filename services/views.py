from django.shortcuts import render
from . models import *
# Create your views here.

def service(request):
    premium_model = {
        'cars': Premium_Car_Model.objects.all()
    }
    return render(request, 'service.html', premium_model)

def premium_car_reservation(request):
    return render(request, 'premium-rental.html')
from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='sign_in')
def service(request):
    premium_model = {
        'cars': Premium_Car_Model.objects.all()
    }
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            purpose = request.POST.get('purpose')
            car_model = request.POST.get('car_model')
            pickup_location = request.POST.get('pickup_location')
            dropoff_location = request.POST.get('dropoff_location')
            pickup_date = request.POST.get('pickup_date')
            pickup_time = request.POST.get('pickup_time')
            dropoff_date = request.POST.get('dropoff_date')
            dropoff_time = request.POST.get('dropoff_time')
            reservation_data = Car_Reservation.objects.create(name=name, email=email, number=phone, purpose=purpose, car_model=car_model,
                                pickup_location=pickup_location, dropoff_location=dropoff_location, pickup_date=pickup_date, pickup_time=pickup_time, dropoff_date=dropoff_date, dropoff_time=dropoff_time)
            success_msg = 'Successfully Booked'
            messages.success(request, success_msg)
            reservation_data.save()
            return redirect('service')
        except Exception as e:
            error_msg = 'Something Wrong'
            messages.error(request, error_msg)
            return redirect('service')
    return render(request, 'service.html', premium_model)

@login_required(login_url='sign_in')
def premium_car_rental(request, pk):
    car_model = {
        'model': Premium_Car_Model.objects.get(pk=pk)
    }
    return render(request, 'premium-rental.html', car_model)

@login_required(login_url='sign_in')
def premium_car_reservation(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            purpose = request.POST.get('purpose')
            car_model = request.POST.get('car_model')
            pickup_location = request.POST.get('pickup_location')
            dropoff_location = request.POST.get('dropoff_location')
            pickup_date = request.POST.get('pickup_date')
            pickup_time = request.POST.get('pickup_time')
            dropoff_date = request.POST.get('dropoff_date')
            dropoff_time = request.POST.get('dropoff_time')
            reservation_data = Premium_Car_Reservation.objects.create(name=name, email=email, number=phone, purpose=purpose, car_model=car_model, pickup_location=pickup_location, dropoff_location=dropoff_location, pickup_date=pickup_date, pickup_time=pickup_time, dropoff_date=dropoff_date, dropoff_time=dropoff_time)
            success_msg = 'Successfully Booked'
            messages.success(request, success_msg)
            reservation_data.save()
            return render(request, 'premium-rental.html')
        except Exception as e:
            error_msg = 'Something Wrong'
            messages.error(request, error_msg)
            return render(request, 'premium-rental.html')
            
from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

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
            reservation_data = Car_Reservation.objects.create(name=name, email=email, number=phone, purpose=purpose, car_model=car_model, pickup_location=pickup_location, dropoff_location=dropoff_location, pickup_date=pickup_date, pickup_time=pickup_time, dropoff_date=dropoff_date, dropoff_time=dropoff_time)
            reservation_data.save()
            subject = "Rental Car Service"
            message = f"Dear {name},\nYou are successfully booked our car reservation Service with Rental. We will get back to you soon.\nHere are your service details:\n\tName: {name}\n\tPhone Number:{phone}\n\tCar Model: {car_model}\n\tPickup Location: {pickup_location}\n\tDropoff Location: {dropoff_location}\n\tPickup Date: {pickup_date}\n\tDropoff Date: {dropoff_date}\nPlease keep this email for your records and do not forward or share any other person.\nTo get started, please visit our website at https://www.rental.pythonanywhere.com/ and use our services.\nFor more details login with Rental.\n\nBest Regards,\nRental Team."
            recipient = email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=True,
            )
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
            reservation_data.save()
            subject = "Rental Premium Car Service"
            message = f"Dear {name},\nYou are successfully booked our premium car reservation Service with Rental. We will get back to you soon.\nHere are your service details:\n\tName: {name}\n\tPhone Number:{phone}\n\tCar Model: {car_model}\n\tPickup Location: {pickup_location}\n\tDropoff Location: {dropoff_location}\n\tPickup Date: {pickup_date}\n\tDropoff Date: {dropoff_date}\nPlease keep this email for your records and do not forward or share any other person.\nTo get started, please visit our website at https://www.rental.pythonanywhere.com/ and use our services.\nFor more details login with Rental.\n\nBest Regards,\nRental Team."
            recipient = email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=True,
            )
            success_msg = 'Successfully Booked'
            messages.success(request, success_msg)
            return render(request, 'premium-rental.html')
        except Exception as e:
            error_msg = 'Something Wrong'
            messages.error(request, error_msg)
            return render(request, 'premium-rental.html')
            
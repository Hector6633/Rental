from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . decorators import unauthenticated_user
from django.core.mail import send_mail
from django.conf import settings
@unauthenticated_user
def sign_up(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            new_account = User.objects.create_user(username=username, email=email, password=password)
            new_account.save()
            subject = "Rental Account Manager"
            message = f"Dear {username},\nYou are successfully created your account with Rental.\nPlease keep this email for your records and do not forward or share any other person.\nTo get started, please visit our website at https://www.rental.pythonanywhere.com/ and use our services.\nFor more details login with Rental.\n\nBest Regards,\nRental Team."
            recipient = email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=True,
            )
            success_msg = 'User Created'
            messages.success(request, success_msg)
            return redirect('sign_in')
        except Exception as e:
            error_msg = 'Something Wrong!'
            messages.error(request, error_msg)
            return redirect('sign_up')
    return render(request, 'sign-up.html')

@unauthenticated_user
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('index')
        else:
            error_msg = 'Invalid User'
            messages.error(request, error_msg)
            return redirect('sign_in')
    return render(request, 'sign-in.html')

@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    success_msg = 'Signout Successfully'
    messages.success(request, success_msg)
    return redirect('sign_in')   
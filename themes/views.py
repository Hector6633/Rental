from django.shortcuts import render, redirect
from . models import Feedback_us
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')
def contact(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            service = request.POST['service']
            subject = request.POST['subject']
            message = request.POST['message']
            feedback_data = Feedback_us.objects.create(name=name, email=email, phone=phone, service=service, subject=subject,message=message)
            feedback_data.save()
            success_msg = "Successfully Registered"
            messages.success(request, success_msg)
            return redirect('contact')
        except Exception as e:
            error_msg = 'Server Error'
            messages.error(request, error_msg)
            return redirect('contact')
    return render(request, 'contact.html')
def page_not_found404(request):
    return render(request, '404.html')

def sign_up(request):
    return render(request, 'sign-up.html')

def sign_in(request):
    return render(request, 'sign-in.html')
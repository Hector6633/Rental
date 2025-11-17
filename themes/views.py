from django.shortcuts import render, redirect
from . models import Feedback_us
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
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
            subject = "Rental Feedback"
            message = f"Dear {name},\nThank you for your feedback. We will get back to you soon.\n\nBest Regards,\nRental Team."
            recipient = email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=True,
            )
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
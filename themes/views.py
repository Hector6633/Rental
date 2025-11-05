from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def page_not_found404(request):
    return render(request, '404.html')

def sign_up(request):
    return render(request, 'sign-up.html')

def sign_in(request):
    return render(request, 'sign-in.html')
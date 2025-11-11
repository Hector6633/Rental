from django.shortcuts import render

# Create your views here.
def premium_rental(request):
    return render(request, 'premium-rental.html')
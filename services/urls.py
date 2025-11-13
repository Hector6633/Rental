from django.urls import path
from . views import *

urlpatterns = [
    path('service/', service, name='service'),
    path('premium-rental<int:pk>/', premium_car_rental, name='premium_car_rental'),
    path('premium-rental/', premium_car_reservation, name='premium_car_reservation'),
]

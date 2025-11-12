from django.urls import path
from . views import *

urlpatterns = [
    path('service/', service, name='service'),
    path('premium-rental/', premium_car_reservation, name='premium_car_reservation'),
]

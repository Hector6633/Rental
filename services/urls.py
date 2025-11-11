from django.urls import path
from . views import *

urlpatterns = [
    path('premium-rental/', premium_rental, name='premium_rental'),
]

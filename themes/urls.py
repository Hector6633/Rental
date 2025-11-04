from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('page_not_found404/', page_not_found404, name='page_not_found404'),
]

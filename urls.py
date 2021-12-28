from django.contrib.auth import logout
from django.urls import path
from .views import about,home,contact, index,login

urlpatterns = [
    path('home',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('index/',index,name='dashboard'),
]

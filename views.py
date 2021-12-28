from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 
#Create your views here.

from rest_framework import generics, serializers
from hospital.models import *
from hospital.serializers import *

class docter(generics.ListCreateAPIView):
    queryset=docter.objects.all()
    serializer_class=docterSerializer

class patient(generics.ListCreateAPIView):
    queryset=patient.objects.all()
    serializer_class=patientSerializer

class appointment(generics.ListCreateAPIView):
    queryset=appointment.objects.all()
    serializer_class=appointmentSerializer






def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html') 

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')

def login(request):
    error=""
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['password']
        user=authenticate(username=u,pasword=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'login.html',d)

def logout(request):
    if not request.user.is_staff:
         return redirect("login")
    logout(request)
    return redirect("login")
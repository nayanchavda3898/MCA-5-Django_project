from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def groundbooking(request):
    return render(request,'groundbooking.html')

def batchregistration(request):
    return render(request,'batchregistration.html')

def registration(request):
    return render(request,'registration.html')
    
def login(request):
    return render(request,'login.html')

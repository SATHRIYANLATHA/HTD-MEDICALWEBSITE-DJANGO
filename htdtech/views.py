from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contactinfo.html')


def admissionguidelines(request):
    return render(request,'admissionguidelines.html')


def previousyearinformation(request):
    return render(request,'previousyearinformation.html')

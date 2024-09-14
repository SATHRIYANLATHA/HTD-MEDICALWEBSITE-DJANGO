from django.urls import path
from . import views



urlpatterns = [

    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("admissionguidelines/", views.admissionguidelines, name="admissionguidelines"),
    path("previousyearinformation/", views.previousyearinformation, name="previousyearinformation"),
    path("notification/",views.notification, name="notification")
    
]

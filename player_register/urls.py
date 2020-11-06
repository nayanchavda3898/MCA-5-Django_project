from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('index',views.index,name="index"),
    path('groundbooking',views.groundbooking,name="groundbooking"),
    path('batchregistration',views.batchregistration,name="batchregistration"),
    path('registration',views.registration,name="registration"),
    path('login',views.login,name="login"),
]

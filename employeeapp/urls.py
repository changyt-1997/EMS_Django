# encoding: utf-8
from django.urls import path,include
from employeeapp import views
app_name = 'employeeapp'

urlpatterns = [
    path('home/',views.home,name = 'home'),
]
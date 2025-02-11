from django.contrib import admin
from django.urls import path, include
from mgr import costomer

urlpatterns = [

    path('customers',customer.dispatcher),
]
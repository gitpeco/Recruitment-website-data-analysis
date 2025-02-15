from django.contrib import admin
from django.urls import path, include
from mgr.customer import dispatcher

urlpatterns = [

    path('customers/',dispatcher),
]
from django.contrib import admin
from django.urls import path, include
from mgr.customer import dispatcher
from mgr import sign_in_out

urlpatterns = [

    path('customers/',dispatcher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
]
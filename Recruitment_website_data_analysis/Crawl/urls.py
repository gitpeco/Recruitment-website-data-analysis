
from django.urls import path
from Crawl.views import listorders,listcustomers

urlpatterns = [
    path('content/', listorders),
    path('customers/', listcustomers),
]
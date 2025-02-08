
from django.urls import path
from Crawl_content.views import listorders,listcustomers

urlpatterns = [


    path('content/', listorders),
    path('customers/', listcustomers),
]
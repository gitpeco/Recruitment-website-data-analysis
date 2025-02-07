
from django.urls import path
from Crawl_content.views import listorders

urlpatterns = [


    path('content/', listorders),

]
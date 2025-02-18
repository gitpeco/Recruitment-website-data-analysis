from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('users/', views.get_users),
    path('users/<int:user_id>/', views.delete_user),
]
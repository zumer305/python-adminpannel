from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user),
    path('list/', views.get_users),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('sign/', views.signin,name='注册页面'),
]
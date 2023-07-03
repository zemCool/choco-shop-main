from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.redirect, name='redirect'),
    path('index/', views.catalog, name='catalog'),
    path('sign_in/', views.sign_user, name='sign_in'),
    path('registration/', views.register_user, name='registration'),
    path('log_out/', views.logout_user, name='logout_user'),
    path('order/<int:pk>', views.create_order, name='create_order'),
]

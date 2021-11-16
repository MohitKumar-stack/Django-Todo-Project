from django.contrib import admin
from django.urls import path
from CRUD_app import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('delete/<int:Id>', views.delete,name='delete'),
]

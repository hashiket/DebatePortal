from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login, name='login'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('register', views.register, name='register'),
    path('adminstrator', views.admin, name='adminstrator'),
    path('addtopic', views.addtopic, name='addtopic'),
    path('alltopic',views.alltopic, name='alltopic'),
    path('alldebater',views.alldebater, name='alldebater'),
    path('debater', views.debater, name='debater'),
    path('view', views.view, name='view'),



]
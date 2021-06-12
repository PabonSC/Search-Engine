
from django.urls import path
from .views import Search, homepage,loginForm,Registration,logoutuser,Search

urlpatterns = [
    path('',homepage,name='home'),
    path('home/',homepage,name='home'),
    path('login/',loginForm,name='login'),
    path('logout/',logoutuser,name='logout'),
    path('register/',Registration,name='register'),
    path('',Search)
]

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('logout/',views.home1,name='LogOut'),
    path('RegDoct/',views.RegDoct,name='RegDoct'),
    path('RegChem/',views.RegChem,name='RegChem'),
    path('RegLabChemist/',views.RegLabChemist,name='RegLabChemist'),
    path('LogDoct/',views.LogDoct,name='LogDoct'),
    path('LogChem/',views.LogChem,name='LogChem'),
    path('LogLabChemist/',views.LogLabChemist,name='LogLabChemist'),
    path('welcome/',views.Welcome,name='welcome'),
    path('welcome/user/',views.user,name='User'),
    path('welcome/patient/',views.patient,name='Patient'),
    path('welcome/table/',views.table,name='Table'),
    path('welcome/history/',views.history,name='History'),
    path('welcome/history/',views.history,name='History'),
    #path('accounts/login/',views.home1,name='History'),
]
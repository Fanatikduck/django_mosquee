from django.urls import path
from . import views
from django.contrib import admin

urlpatterns=[
    path('formulaire',views.formulaire, name= 'formulaire'),
    path('success',views.success,name='success'),
    path('actualite', views.evenement, name='actualite'),
    path('cours',views.cours, name='cours')
]
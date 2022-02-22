
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.index),
    path('nowayhome',views.index1),
    path('mutiverseofmadness',views.index3)

   
]
    
    

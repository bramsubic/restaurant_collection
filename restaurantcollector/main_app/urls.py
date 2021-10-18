from django.urls import path #will be used to deine each route 
from . import views

urlpatterns = [ #will hold each route we define for main_app
    path('', views.home, name='home'),
]
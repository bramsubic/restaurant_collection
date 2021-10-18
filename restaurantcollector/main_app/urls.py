from django.urls import path #will be used to deine each route 
from . import views

#will hold each route we define for main_app
urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
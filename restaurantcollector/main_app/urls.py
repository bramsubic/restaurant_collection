from django.urls import path #will be used to deine each route 
from . import views

#will hold each route we define for main_app
urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:restaurant_id>/', views.restaurants_detail, name='detail'),
]
from django.urls import path #will be used to deine each route 
from . import views

#will hold each route we define for main_app
urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:restaurant_id>/', views.restaurants_detail, name='detail'),
    path('restaurants/new', views.restaurants_new),
    path('restaurants/submit/', views.restaurants_create),  

  # these urls are connected to view functions
    path('restaurants/<int:restaurant_id>/delete/', views.restaurants_delete, name='restaurants_delete'),
    path('restaurants/<int:restaurant_id>/edit/', views.restaurants_edit, name='restaurants_edit'), #show the form
    path('restaurants/<int:restaurant_id>/update/', views.restaurants_update, name='restaurants_update') #handle form data
]
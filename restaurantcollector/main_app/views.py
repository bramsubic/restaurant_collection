from django.shortcuts import render, redirect 
from .models import Restaurant

# View functions
def restaurants_delete(request,restaurant_id):
  # get ahold of the resto
  r = Restaurant.objects.get(id=restaurant_id)  
  r.delete() # <--- django ORM command to delete from DB
  return redirect('/restaurants')

def restaurants_new(request):
  return render(request, 'restaurants/new.html')

# show form
def restaurants_edit(request, restaurant_id):
  r = Restaurant.objects.get(id= restaurant_id)
  print("we are updating resto", r)
  return render(request, 'restaurants/edit.html', {
    'restaurant':r
  })

# handle form data
def restaurants_update(request, restaurant_id):
  r = Restaurant.objects.get(id = restaurant_id)
  r.name = request.POST['name']
  r.neighbourhood = request.POST['neighbourhood']
  r.cost = request.POST['cost']
  r.cuisine = request.POST['cuisine']
  r.suggestion = request.POST['suggestion']
  r.save() # <---- save to db
  return redirect(f'/restaurants/{r.id}')

def restaurants_create(request):
  # request.POST is django's req.body 
  # it contains incoming form data
  print("ctrl hit")
  print(request.POST)
  r = Restaurant.objects.create(
    name= request.POST['name'],
    neighbourhood = request.POST['neighbourhood'],
    cost = request.POST['cost'],
    cuisine = request.POST['cuisine'],
    suggestion = request.POST['suggestion']
  )
  # create a RESTO object out of the 
  #    incoming data
  # redirect to a different URL
  return redirect(f'/restaurants/{r.id}')

#  defines a view func that responds to browser's HTTP request 
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def restaurants_index(request):
  restaurants = Restaurant.objects.all()
  return render(request, 'restaurants/index.html', { 'restaurants': restaurants })

def restaurants_detail(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  return render(request, 'restaurants/detail.html', { 'restaurant': restaurant })
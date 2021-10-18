from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Restaurant:  
  def __init__(self, name, neighbourhood, cost, cuisine, suggestion):
    self.name = name
    self.neighbourhood = neighbourhood
    self.cost = cost
    self.cuisine = cuisine
    self.suggestion = suggestion

restaurants = [
  Restaurant('Konjiki Ramen', 'North York', '$$', 'Japanese', 'Spicy Red Tonkotsu Ramen'),
  Restaurant('Foxley', 'Dundas St W', '$$', 'Asian & Pan-Latin', 'Arctic Char Ceviche with Green Apple and Ginger'),
  Restaurant('Raku', 'Queen St W', '$$', 'Japanese', 'Niku')
]
# Define the home view
#  defines a view func that responds to browser's HTTP request 
def home(request):
  return HttpResponse('<h1>Welcome to the Resto Collective</h1>')

def about(request):
  return render(request, 'about.html')

def restaurants_index(request):
  return render(request, 'restaurants/index.html', { 'restaurants': restaurants })
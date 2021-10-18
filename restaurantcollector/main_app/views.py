from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
#  defines a view func that responds to browser's HTTP request 
def home(request):
  return HttpResponse('<h1>Welcome to the Resto Collective</h1>')

def about(request):
  return render(request, 'about.html')
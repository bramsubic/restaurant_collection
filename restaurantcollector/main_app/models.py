from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    neighbourhood = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    suggestion = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name
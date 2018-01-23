from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  #Variable length
    county = models.CharField(max_length=30)    
    
		

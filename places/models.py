from django.db import models
from django.conf import settings
from django.conf.urls.static import static
import os

class Item(models.Model):
    site_media = static(settings.STATIC_URL)
    title = models.CharField(max_length=200)
    description = models.TextField()  #Variable length
    county = models.CharField(max_length=30)    
    image = models.ImageField(upload_to = site_media ,default = '')
    

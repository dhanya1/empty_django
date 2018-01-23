from django.contrib import admin
from .models import Item

class ItemsDisplay(admin.ModelAdmin):
	list_display = ['title','county']
admin.site.register(Item, ItemsDisplay)


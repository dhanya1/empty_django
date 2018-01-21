from django.contrib import admin
from .models import Item

class ItemsDisplay(admin.ModelAdmin):
	list_display = ['title','amount']
admin.site.register(Item, ItemsDisplay)


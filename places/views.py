from django.shortcuts import render
from django.http import Http404

from places.models import Item
	
def index(request):
	items = Item.objects.exclude(county='')
	return render(request,'places/index.html',{
	'items':items,
	})

def item_detail(request,id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request,'places/item_detail.html',{
	'item':item,
	})
	

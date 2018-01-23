from django.conf.urls import include, url
from django.contrib import admin
from places import views
# 1.Home page matching '/' as request
#Matching the namespace <id> followed by id number
#Starting with admin / will go to admin.site.urls module.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/',views.item_detail, name = 'item_detail'),
    url(r'^admin/', include(admin.site.urls)),
]

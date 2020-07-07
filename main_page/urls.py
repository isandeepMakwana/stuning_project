from django.urls import path
from . import views
from .views import item_list

urlpatterns = [
    path('',views.index, name='index'),
    path('items/?$',item_list, name='item-list'),
    path('items/(?P<pk>[0-9]+)/?$', item_list, name='item-detail')    
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('items/?$',views.item.ItemList.as_viwe(), name='item-list'),
    path('items/(?P<pk>[0-9]+)/?$', views.item.ItemList.as_viwe())    
]
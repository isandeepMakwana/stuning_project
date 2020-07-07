from django.contrib import admin
from .models import Item


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'like_count']
    search_fields = ['title']
    



admin.site.register(Item, ItemAdmin)

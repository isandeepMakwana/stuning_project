from django.contrib import admin
from .models import Item


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'like_count', 'full_title']
    search_fields = ['title']




admin.site.register(Item, ItemAdmin)

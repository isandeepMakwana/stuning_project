from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    """
    This is the moodel for items.
    """
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank =True, null=True)
    like_count = models.IntegerField(default=0)
    img = models.ImageField()
    #owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def full_title(self):
        return "%s :  %s" %(self.title, self.subtitle)
        
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=255)
    subtitle = serializers.CharField(required=False, allow_blank=True, max_length=255)
    created_at =serializers.DateTimeField(read_only = True)
    updated_at = serializers.DateTimeField(read_only =True)

    
    def create(self, validated_data):

        return Item.objects.create(**validated_data)
from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description', 'food_type')
        model = Food
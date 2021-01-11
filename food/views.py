from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializer import FoodSerializer
from .models import Food

# Create your views here.

class FoodListView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetailsView(RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

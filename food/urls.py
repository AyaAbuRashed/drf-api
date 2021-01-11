from django.contrib import admin
from django.urls import path, include
from .views import FoodDetailsView, FoodListView

urlpatterns = [
    path('', FoodListView.as_view(), name='food'),
    path('<int:pk>/', FoodDetailsView.as_view(), name='Food_details'),
]
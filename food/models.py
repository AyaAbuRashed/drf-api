

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    food_type = models.CharField(max_length=64)
    def __str__(self):
        return self.title

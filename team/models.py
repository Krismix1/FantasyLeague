from django.db import models


# Create your models here.

class Footballer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    price = models.FloatField
    is_injured = models.BooleanField(default=False)
    position = models.CharField(max_length=3)
    real_team = models.CharField(max_length=50)
    kit_number = models.PositiveSmallIntegerField
    game_week_points = models.PositiveIntegerField
    total_points = models.PositiveIntegerField

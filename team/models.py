from django.db import models


# Create your models here.

class Footballer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    is_injured = models.BooleanField(default=False)
    position = models.CharField(max_length=3)
    real_team = models.CharField(max_length=50)
    kit_number = models.PositiveSmallIntegerField(default=0)
    game_week_points = models.PositiveIntegerField(default=0)
    total_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.real_team + " " + str(self.price)

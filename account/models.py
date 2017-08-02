from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=50)
    favourite_team = models.CharField(max_length=100)
    wallet = models.FloatField(default=100)
    game_week_points = models.IntegerField(default=100)
    total_points = models.IntegerField(default=0)

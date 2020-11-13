from django.db import models
from django.contrib.auth.models import User


class Plateau(models.Model):
    x_length = models.PositiveIntegerField()
    y_height = models.PositiveIntegerField()


class Rover(models.Model):
    # automatically increments according to available IDs
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    # foreign key to reference User object
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    starting_position_x = models.PositiveIntegerField()
    starting_position_y = models.PositiveIntegerField()
    starting_direction = models.CharField(max_length=1)
    movement_instructions = models.CharField(max_length=100)


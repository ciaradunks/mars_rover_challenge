from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Plateau(models.Model):
    x_length = models.PositiveIntegerField()
    y_height = models.PositiveIntegerField()


class Rover(models.Model):
    # automatically increments according to available IDs
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    # maybe there is a more specific way to reference the user id e.g. User.id?
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    starting_position_x = models.PositiveIntegerField()
    starting_position_y = models.PositiveIntegerField()
    starting_direction = models.CharField(max_length=1)
    movement_instructions = models.CharField(max_length=100)


class RoverInstructions(models.Model, Plateau, Rover):
    AVAILABLE_COMMANDS = {
        'M': 'move',
        'L': 'turn_left',
        'R': 'turn_right',
    }

    DIRECTIONS = {
        'N': 1,
        'E': 2,
        'S': 3,
        'W': 4,
    }

    def __init__(self):
        self.plateau = Plateau.x_length, Plateau.y_height
        self.position.x = Rover.starting_position_x
        self.position.y = Rover.starting_position_y
        self.heading = Rover.starting_direction

    def current_position(self):
        return'{} {} {}'.format(self.position.x,
                                self.position.y,
                                self.heading
                                )

    def get_heading(self):
        directions = list(self.DIRECTIONS.keys())


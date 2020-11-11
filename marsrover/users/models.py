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
        self.plateau.x = Plateau.x_length
        self.plateau.y = Plateau.y_height
        self.position.x = Rover.starting_position_x
        self.position.y = Rover.starting_position_y
        self.direction = Rover.starting_direction

    def current_position(self):
        return'{} {} {}'.format(self.position.x,
                                self.position.y,
                                self.direction
                                )

    def process(self, commands):
        for i in range(len(commands)):
            self.run_command(commands[i])

    def run_command(self, command):
        if 'L' == command:
            self.turn_left()
        elif 'R' == command:
            self.turn_right()
        elif 'M' == command:
            if not self.move():
                print("Where are you trying to go?")
        else:  # Unrecognized instruction
            print("Wrong parameters!..")

    def move(self):
        if not self.plateau.move_available(self.position):
            return False
        # Assume that the square directly North from (x, y) is (x, y+1).
        if self.DIRECTIONS['N'] == self.direction:
            self.position.y += 1
        elif self.DIRECTIONS['E'] == self.direction:
            self.position.x += 1
        elif self.DIRECTIONS['S'] == self.direction:
            self.position.y -= 1
        elif self.DIRECTIONS['W'] == self.direction:
            self.position.x -= 1

        return True

    def turn_left(self):
        self.direction = self.DIRECTIONS['W'] if (self.direction - 1) < self.DIRECTIONS['N'] else self.direction - 1

    def turn_right(self):
        self.direction = self.DIRECTIONS['N'] if (self.direction + 1) > self.DIRECTIONS['W'] else self.direction + 1
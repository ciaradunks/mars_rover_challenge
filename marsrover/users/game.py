"""from .models import Plateau, Rover


class RoverInstructions(rover_dict):
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
        self.commands = Rover.movement_instructions

    def current_position(self):
        return'{} {} {}'.format(self.position.x,
                                self.position.y,
                                self.direction
                                )

    def process(self):
        for i in range(len(self.commands)):
            self.run_command(self.commands[i])

    def run_command(self):
        if 'L' == self.command:
            self.turn_left()
        elif 'R' == self.command:
            self.turn_right()
        elif 'M' == self.command:
            if not self.move():
                print("Where are you trying to go?")
        else:  # Unrecognized instruction
            print("Wrong parameters!..")

    def move(self):
        if not self.plateau.move_available(self.position):
            return False
        # Assume that the square directly North from (x, y) is (x, y+1).
        if self.DIRECTIONS['N'] == self.direction:
            self.position.y += 1y
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
        self.direction = self.DIRECTIONS['N'] if (self.direction + 1) > self.DIRECTIONS['W'] else self.direction + 1"""
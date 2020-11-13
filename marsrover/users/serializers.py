from rest_framework import serializers
from .models import Rover, Plateau


# A way of serializing/deserializing the rover instances into json instances
# ModelSerializer is shortcut for creating serializer classes from model
class RoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rover
        fields = ['id', 'name', 'user_id', 'starting_position_x',
                  'starting_position_y', 'starting_direction', 'movement_instructions']


class PlateauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plateau
        fields = ['x_length', 'y_height']



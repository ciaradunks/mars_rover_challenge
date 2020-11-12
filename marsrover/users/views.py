from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse
import requests
from django.contrib.auth.forms import UserCreationForm
from users.models import Rover, Plateau
from users.serializers import RoverSerializer, PlateauSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
#from users.game import RoverInstructions
from django.contrib.auth.models import User
import json

# rendering -> takes intermediate representation of template and context,
# and turns it into final byte stream that can be served to client

# POST is used for creating a new rover, posting to the parent and then the
# service takes care of associating new rover with parent

# GET is used to retrieve a rover without changing it

# PUT is used (in this case) to update a rover

# DELETE is used to delete a rover

# NOTE: class based views are cleaner (less lines of code) but more advanced

def home_view(request):
    return render(request, 'users/home.html')


def register_view(request):
    # if view is displayed by browser, a template called users/register.html
    # will be rendered
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {'form': UserCreationForm}
        )
    elif request.method == "POST":
        # if the form is submitted, Django will attempt to create a user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # new user is created and saved to database
            user = form.save()
            # user is logged in
            login(request, user)
            # directs user to rover page ToDo: change
            return redirect(reverse("rovers"))


class PlateauViewset(viewsets.ModelViewSet):
    queryset = Plateau.objects.all()
    serializer_class = PlateauSerializer


class RoverViewset(viewsets.ModelViewSet):
    queryset = Rover.objects.all()
    serializer_class = RoverSerializer


def rover_view(request):
    # change to entire list of rovers then pick out the ones with the right user id
    response = requests.get('http://127.0.0.1:8000/api/v1/rovers/')
    rovers = response.json()
    # filter list based on user id, which gets passed onto the view
    filtered_rovers = [x for x in rovers if x['user_id'] == User]
    return render(request, 'users/rovers.html', {'rovers': rovers})


#game = RoverInstructions()

# figure out how to get rover variable
# put variable
# put variable to identify rover on router (api.py)

"""    rover_info = {'id': rovers['id'],
                  'name': rovers['name'],
                  'user_id': rovers['user_id'],
                  'starting_position_x': rovers['starting_position_x'],
                  'starting_position_y': rovers['starting_position_y'],
                  'starting_direction': rovers['starting_direction'],
                  'movement_instructions': rovers['movement_instructions']
                  }"""
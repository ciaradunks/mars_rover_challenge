from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse
import requests
from django.contrib.auth.forms import UserCreationForm
from users.models import Rover, Plateau
from users.serializers import RoverSerializer, PlateauSerializer
from rest_framework import viewsets


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
            # directs user to rover page
            return redirect(reverse("rovers"))


# Viewsets are almost the same as Views, except they provide operations such as
# retireve or update instead of method handlers such as get and put
# ModelViewSet is chosen to get the complete set of default read and write operations
class PlateauViewset(viewsets.ModelViewSet):
    queryset = Plateau.objects.all()
    serializer_class = PlateauSerializer


class RoverViewset(viewsets.ModelViewSet):
    queryset = Rover.objects.all()
    serializer_class = RoverSerializer


def rover_list_view(request):
    # maybe a different way to do this?
    response = requests.get('http://127.0.0.1:8000/api/v1/rovers/')
    rovers_list = response.json()
    # filter list based on user id, which gets passed onto the view
    filtered_rovers_list = [x for x in rovers_list if x['user_id'] == request.user.id]
    return render(request, 'users/rovers.html', {'rovers': filtered_rovers_list})


"""def run_game_view(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/rovers/')
    rovers_list = response.json()
    # filter list based on user id, which gets passed onto the view
    filtered_rovers_list = [x for x in rovers_list if x['user_id'] == request.user.id]

    for rover in filtered_rovers_list:
        game = RoverInstructions(rover)
        game_results = {}
        game_results[rover['id']] = game.process()"""




from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from users.models import Rover, Plateau
from users.serializers import RoverSerializer, PlateauSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets


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


class RoverViewset(viewsets.ModelViewSet):
    queryset = Rover.objects.all()
    serializer_class = RoverSerializer


class PlateauViewset(viewsets.ModelViewSet):
    queryset = Plateau.objects.all()
    serializer_class = PlateauSerializer
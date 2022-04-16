from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect('recommender/')
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('recommender/')
        else:
            return render(request, "authentication/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "authentication/login.html")


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "authentication/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
        # hadeling if a user already exists
            return render(request, "authentication/register.html", {
                "message": "Username already taken."
            })
        except ValueError:
        # handling if the user didnt fill in all the fields
            return render(request, "authentication/register.html", {
                "message": "Please fill all required fields."
            })

        login(request, user)
        return redirect('recommender/')
    else:
        return render(request, "authentication/register.html")
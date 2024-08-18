from django.shortcuts import render, redirect
from .models import Profile, Tweet
from django.contrib import messages
from .forms import Post, SignUp, ProfilePic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form = Post(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()

                messages.success(request, ('Tweet has been posted successfully.'))
                return redirect('home')

        tweets = Tweet.objects.all().order_by("-created")
        return render(request, 'home.html', {"tweets":tweets, "form":form})
    else:
        tweets = Tweet.objects.all().order_by("-created")
        return render(request, 'home.html', {"tweets":tweets})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles": profiles})
    else:
        messages.success(request, ('You must be logged in to view this page! Please login.'))
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=pk)
        tweets = Tweet.objects.filter(user_id=pk).order_by("-created")

        if request.method == "POST":
            current_user = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user.follows.remove(profile)
            else:
                current_user.follows.add(profile)

            current_user.save()
        return render(request, 'profile.html', {"profile": profile, "tweets":tweets})
    else:
        messages.success(request, ('You must be logged in to view this page! Please login.'))
        return redirect('home')
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged in successfully")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging you in :(")
            return redirect('login')
    else:
        return render(request, 'login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out. Sorry to see you go!")
    return redirect('home')

def register_user(request):
    form = SignUp()
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, ("You've been registered successfully!"))
            return redirect('home')
    
    return render(request, 'register.html', {"form":form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user_id=request.user.id)
        user_form = SignUp(request.POST or None, request.FILES or None, instance=current_user)
        picture_form = ProfilePic(request.POST or None, request.FILES or None, instance=profile_user)

        if user_form.is_valid() and picture_form.is_valid():
            user_form.save()
            picture_form.save()
            login(request, current_user)
            messages.success(request, ("Your profile has been updated!"))
            return redirect('home')
        return render(request, 'update.html', {"user_form":user_form, "picture_form":picture_form})
    else:
        messages.success(request, ("You have to be logged in to view this page."))
        return redirect('home')

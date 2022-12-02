
from django import urls
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from PostBackend.models import Tweet

from .forms import UserForm, UserProfileForm
from .models import Profile


# Create your views here.
def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.info(request, 'login successful')
                login(request, user)
                return redirect( 'home')
            else:
                messages.error(request, 'Credential Not Found')  
                return redirect('login')
        except:
            messages.error(request, 'Credential Not Found')  
    return render(request, 'registration/login.html')

def UserLogout(request):
    logout(request)
    return redirect( 'home')

def UserRegistration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'registration/signup.html')

def ResetUserPassword(request):
    if request.method == 'POST':
        user = request.user
        new_password = request.POST
        user.set_password(new_password)
    return render(request, 'registration/reset_password.html')

def UserProfile(request, pk):
    tweet_user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=tweet_user)
    user_tweet = Tweet.objects.filter(user=tweet_user)
    if profile.follower.filter(id=request.user.id).exists():
        isFollowing = True
    else:
        isFollowing = False
    context = {'tweet_user': tweet_user, 'user_tweet': user_tweet, 
               'profile': profile, 'isFollowing': isFollowing}
    return render(request, 'registration/Profile.html', context)

@login_required
def EditUserProfile(request):
    form = UserProfileForm(instance=request.user.profile)
    User_Form = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        User_Form = UserForm(request.POST,instance=request.user)
        if form.is_valid() and User_Form.is_valid():
            form.save()
            User_Form.save()
            messages.info(request, 'Profile save')
            return redirect('home')
        else:
            messages.error(request, 'invalid')
    context={ 'UserForm': User_Form, 'form':form}
    return render(request, 'registration/user_profile.html', context)

def followUser(request, pk):
    _user = User.objects.get(id=pk)
    user = Profile.objects.get(user=_user)
    if user.follower.filter(id=request.user.id).exists():
        user.follower.remove(request.user)
    else:
        user.follower.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
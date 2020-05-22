from django.shortcuts import render, redirect
from user.forms import UserSignUp
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# User creation account views
def register(request):
    if request.method == "POST":
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserSignUp()

    context = {
        'form': form
    }
    return render(request, 'user/registration.html', context)

def login_request(request):
    error = "Fill in details correctly"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            error = 'incorrrect username or password. Try again'
    context = {
        'error': error
        }
    return render(request, 'user/login.html', context) 

def logout_request(request):
    logout(request)
    return redirect('home')
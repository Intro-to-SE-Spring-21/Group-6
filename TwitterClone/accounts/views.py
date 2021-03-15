from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Account
# Create your views here.


def loginUser(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request=request, template_name='login.html', context={'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                print('User does not exist')
        else:
            return render(request=request, template_name='login.html', context={'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            passwordPreEncrypt = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=passwordPreEncrypt)
            if user is not None:
                addUserToDB(username)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                print('Something went wrong')
    else:
        form = UserCreationForm()
    return render(request=request, template_name='register.html', context={'form': form})


def logoutUser(request):
    logout(request)
    return redirect('/accounts/login')


def addUserToDB(username):
    newAccount = Account(username=username)
    newAccount.save()
    return

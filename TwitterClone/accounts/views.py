from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Account, Following
from tweets.views import getAllPostedTweets
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

                return HttpResponseRedirect("/accounts/user/page/?user=" + username)

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

                return HttpResponseRedirect("/accounts/user/page/?user=" + username)

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
    return True


def currentUserID(request):
    accountReturned = Account.objects.get(username=request.user.username)
    if (accountReturned):
        return accountReturned
    return False


def getAllFollowedUsers(userAccount):
    return list(Following.objects.filter(follower=userAccount).values_list('following', flat=True))


def followUser(followerUser, toFollowUser):
    followerQuerySet = Following.objects.filter(
        follower=followerUser, following=toFollowUser)
    if followerQuerySet.count() > 0:
        followerQuerySet.delete()
    else:
        followerInstance = Following(
            follower=followerUser, following=toFollowUser)
        followerInstance.save()


def userPageRequest(request, userAccount):
    return render(request, 'accounts.html', {'account': userAccount, 'tweets': getAllPostedTweets(userAccount.userID)})

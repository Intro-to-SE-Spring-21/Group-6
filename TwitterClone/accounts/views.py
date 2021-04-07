from django.shortcuts import render, redirect, HttpResponseRedirect, Http404
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Account, Following
from tweets.models import Tweet, tweetForm
from tweets.views import createTweet, getAllLikedTweets, getAllPostedTweets, likeUserTweet
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

                return HttpResponseRedirect('/page/' + username)

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

                return HttpResponseRedirect("/page/" + username)

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


def userPageRequest(request, username):
    try:
        userAccount = Account.objects.get(username=username)
        viewingAccount = currentUserID(request)
    except:
        raise Http404("User not found")

    if request.method == 'POST':
        if "submitTweet" in request.POST:
            form = tweetForm(request.POST, request.FILES)
            if form.is_valid():
                createTweet(userAccount, form.cleaned_data['message'], form.cleaned_data['media'])
        elif "likeButton" in request.POST:
            tweetInstance = Tweet.objects.get(
                tweetID=request.POST["likeButton"])
            likeUserTweet(viewingAccount, tweetInstance)

        elif "followButton" in request.POST:
            toFollowUser = Account.objects.get(
                userID=request.POST["followButton"])
            followUser(viewingAccount, toFollowUser)

        elif "changeProfile" in request.POST:
            file = request.FILES['newProfile']
            viewingAccount.profilePicture = file
            viewingAccount.save()

        return HttpResponseRedirect("/page/" + userAccount.username)
    form = tweetForm

    context = {
        'viewingAccount': viewingAccount,
        'userAccount': userAccount,
        'form': form,
        'tweets': reversed(getAllPostedTweets(userAccount.userID)),
        'likedTweets': getAllLikedTweets(viewingAccount),
        'followed': getAllFollowedUsers(viewingAccount),
    }

    print(request.user.username, userAccount.username)

    return render(request=request, template_name='accounts.html', context=context)


def search(request):
    print("Hello")
    print(request.GET)
    if request.is_ajax():
        searchResults = [{'label': accountItem.username, 'url': '/page/' + accountItem.username} for accountItem in list(Account.objects.filter(username__icontains=request.GET.get('term')))]
        
        return JsonResponse(searchResults, safe=False)
    return JsonResponse([], safe=False)
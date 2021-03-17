from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from accounts.models import Account
from tweets.models import tweetForm, likeTweet, Tweet
from tweets.views import createTweet, getAllTweets, getAllLikedTweets, likeUserTweet
from accounts.views import currentUserID, getAllFollowedUsers, followUser

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        form = tweetForm

        user = currentUserID(request)
        if request.method == "POST":
            if "submitTweet" in request.POST:
                form = tweetForm(request.POST)
                if form.is_valid():
                    createTweet(
                        user, form.cleaned_data["message"], form.cleaned_data["media"])
            elif "likeButton" in request.POST:
                tweetInstance = Tweet.objects.get(
                    tweetID=request.POST["likeButton"])
                likeUserTweet(user, tweetInstance)
            elif "followButton" in request.POST:
                toFollowUser = Account.objects.get(
                    userID=request.POST["followButton"])
                followUser(user, toFollowUser)
            return HttpResponseRedirect("/")

        tweets = reversed(getAllTweets())
        likedTweets = getAllLikedTweets(user)
        followedUsers = getAllFollowedUsers(user)
        print(followedUsers)

        context = {
            'name': request.user.username,
            'userID': user.userID,
            'form': form,
            'tweets': tweets,
            'likedTweets': likedTweets,
            'followed': followedUsers,
        }
        return render(request=request, template_name='index.html', context=context)
    else:
        return render(request=request, template_name='unauthenticated.html', context={'name': None})

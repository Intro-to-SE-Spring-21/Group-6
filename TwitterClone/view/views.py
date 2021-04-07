from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from accounts.models import Account
from tweets.models import tweetForm, likeTweet, Tweet
from tweets.views import createTweet, getAllFollowedTweets, getAllLikedTweets, likeUserTweet
from accounts.views import currentUserID, getAllFollowedUsers, followUser, userPageRequest

# Create your views here.


def index(request):
    print("Testing")
    if request.user.is_authenticated:

        user = currentUserID(request)
        if request.method == "POST":
            if "likeButton" in request.POST:
                tweetInstance = Tweet.objects.get(
                    tweetID=request.POST["likeButton"])
                likeUserTweet(user, tweetInstance)

            elif "followButton" in request.POST:
                toFollowUser = Account.objects.get(
                    userID=request.POST["followButton"])
                followUser(user, toFollowUser)

            return HttpResponseRedirect("/")

        tweets = reversed(getAllFollowedTweets(user, getAllFollowedUsers(user) + [user]))
        likedTweets = getAllLikedTweets(user)
        followedUsers = getAllFollowedUsers(user)

        context = {
            'name': request.user.username,
            'userID': user.userID,
            'tweets': tweets,
            'likedTweets': likedTweets,
            'followed': followedUsers,
        }
        return render(request=request, template_name='index.html', context=context)
    else:
        return HttpResponseRedirect("/accounts/register/")


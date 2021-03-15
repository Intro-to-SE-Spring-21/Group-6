from django.shortcuts import render
from django.http import HttpResponse
from tweets.models import tweetForm, likeTweet, Tweet
from tweets.views import createTweet, getAllTweets, getAllLikedTweets, likeUserTweet
from accounts.views import currentUserID

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        form = tweetForm

        user = currentUserID(request)
        if request.method == "POST":
            if "submitTweet" in request.POST:
                form = tweetForm(request.POST)
                if form.is_valid():
                    if(createTweet(user, form.cleaned_data["message"], form.cleaned_data["media"])):
                        form = tweetForm
                        pass #if create tweet success
                    else:
                        pass #if create tweet fail
            elif "likeButton" in request.POST:
                tweetInstance = Tweet.objects.get(tweetID = request.POST["likeButton"])
                likeUserTweet(user, tweetInstance)
                

        tweets = getAllTweets(request)
        likedTweets = getAllLikedTweets(user)
        
        context = {
            'name': request.user.username,
            'form': form,
            'tweets': tweets,
            'likedTweets': likedTweets,
        }
        return render(request=request, template_name='index.html', context=context)
    else:
        return render(request=request, template_name='unauthenticated.html', context={'name': None})


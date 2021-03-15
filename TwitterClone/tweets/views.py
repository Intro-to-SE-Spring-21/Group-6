from django.shortcuts import render

from .models import Tweet  # https://stackoverflow.com/questions/35602049/how-to-insert-data-to-django-database-from-views-py-file
import string  # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits

# Create your views here.


def createTweet(account, messageText, mediaLink):
    tweetInstance = Tweet(userID = account, message = messageText, media = mediaLink, numLikes = 0)
    if (tweetInstance):
        tweetInstance.save()
        return True
    return False

def getAllTweets(request):
    allTweets = Tweet.objects.all()
    return allTweets
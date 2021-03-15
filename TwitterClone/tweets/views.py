from django.shortcuts import render

from .models import Tweet  # https://stackoverflow.com/questions/35602049/how-to-insert-data-to-django-database-from-views-py-file
import string  # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits

# Create your views here.


def createTweet(request, account, messageText, mediaLink):
    tweet_instance = Tweet.objects.create(userID = account, message = messageText, media = mediaLink, numLikes = 0)
    return render(request, 'tweets/created.html')

def getAllTweets(request):
    allTweets = Tweet.objects.all()
    return allTweets
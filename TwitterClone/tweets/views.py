from django.shortcuts import render

from .models import Tweet  # https://stackoverflow.com/questions/35602049/how-to-insert-data-to-django-database-from-views-py-file
import string  # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
import random

# Create your views here.


def createTweet(request, account, messageText, mediaLink):
    tweet_instance = Tweet.objects.create(tweetID = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N)), userID = account, message = messageText, media = mediaLink, numLikes = 0)
    return render(request, 'tweets/created.html')

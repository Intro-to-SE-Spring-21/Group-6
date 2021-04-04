from django.shortcuts import render

# https://stackoverflow.com/questions/35602049/how-to-insert-data-to-django-database-from-views-py-file
from .models import Tweet, likeTweet
import string  # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits

# Create your views here.


def createTweet(account, messageText, mediaLink):
    tweetInstance = Tweet(
        userID=account, message=messageText, media=mediaLink, numLikes=0)
    if (tweetInstance):
        tweetInstance.save()
        return True
    return False


def getAllTweets():
    allTweets = Tweet.objects.all()
    return allTweets


def getAllLikedTweets(user):
    try:
        likedTweetsIDs = list(likeTweet.objects.filter(
            userID=user).values_list('tweetID', flat=True))
        return likedTweetsIDs
    except:
        return []


def likeUserTweet(userID, tweetID):
    likeQuerySet = likeTweet.objects.filter(userID=userID, tweetID=tweetID)
    if likeQuerySet.count() > 0:
        likeQuerySet.delete()
    else:
        likeTweetInstance = likeTweet(userID=userID, tweetID=tweetID)
        likeTweetInstance.save()

        
# https://docs.djangoproject.com/en/3.1/topics/db/queries/
def searchTweets(message):
    searched = Tweet.objects.filter(message=message)
    return searched

def getAllPostedTweets(user):
    try:
        postedTweetsIDs = list(Tweet.objects.filter(userID=user).values_list('tweetID', flat=True))
        return postedTweetsIDs
    except:
        return []

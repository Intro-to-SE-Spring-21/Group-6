from django.db import models
from django.forms import ModelForm, HiddenInput
import uuid
from accounts.models import Account
# Create your models here.


class Tweet(models.Model):
    tweetID = models.CharField(
        max_length=10, primary_key=True, unique=True, default=uuid.uuid4)
    userID = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    media = models.ImageField(upload_to="gallery", blank=True)
    numLikes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def getUsername(self):
        return self.userID.username

    @property
    def getUserID(self):
        return self.userID.userID

    @property
    def getUserProfilePic(self):
        return self.userID.profilePicture
    
    @property
    def getNumberOfLikes(self):
        return len(likeTweet.objects.filter(tweetID=self))


class likeTweet(models.Model):
    userID = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    tweetID = models.ForeignKey('tweets.Tweet', on_delete=models.CASCADE)


class tweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['message', 'media']

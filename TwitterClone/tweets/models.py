from django.db import models

# Create your models here.


class Tweet(models.Model):

    # Fields
    tweetID = models.CharField(max_length=10, primary_key=True)
    userID = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    message = models.TextField()
    media = models.ImageField()
    numLikes = models.IntegerField()

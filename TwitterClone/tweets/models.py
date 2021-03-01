from django.db import models

# Create your models here.

class Account(models.Model):

    # Fields
    userID = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=20)
    following = models.ForeignKey('self', on_delete=models.CASCADE)
    followers = models.ForeignKey('self', on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    securityQuestion = models.CharField(max_length=20)
    securityAnswer = models.CharField(max_length=20)

class Tweet(models.Model):

    # Fields
    tweetID = models.CharField(max_length=10, primary_key=True)
    userID = models.ForeignKey('Account', on_delete=models.CASCADE)
    message = models.TextField()
    media = models.ImageField()
    numLikes = models.IntegerField()

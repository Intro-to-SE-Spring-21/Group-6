from django.db import models

# Create your models here.


class Account(models.Model):

    # Fields
    userID = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    securityQuestion = models.CharField(max_length=20)
    securityAnswer = models.CharField(max_length=20)


class Following(models.Model):

    # Fields
    follower = models.ForeignKey('Account', on_delete=models.CASCADE)
    following = models.ForeignKey('Account', on_delete=models.CASCADE)

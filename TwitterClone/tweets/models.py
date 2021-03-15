from django.db import models
from django.forms import ModelForm
import uuid
# Create your models here.


class Tweet(models.Model):

    # Fields
    tweetID = models.CharField(
        max_length=10, primary_key=True, unique=True, default=uuid.uuid4())
    userID = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    media = models.ImageField(blank=True)
    numLikes = models.IntegerField(default=0)

class tweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['message', 'media']

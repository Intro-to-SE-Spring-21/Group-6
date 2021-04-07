from django.contrib import admin
from .models import Tweet, likeTweet
# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    list_display = ('tweetID', 'userID', 'message', 'media', 'numLikes', 'created')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('tweetID', 'userID')

admin.site.register(Tweet, TweetAdmin)
admin.site.register(likeTweet, LikeAdmin)
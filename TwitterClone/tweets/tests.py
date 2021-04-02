from django.test import TestCase
from .models import Tweet, likeTweet
from accounts.models import Account
from .views import createTweet, getAllTweets, getAllLikedTweets, likeUserTweet
# Create your tests here.


class TweetsTestCase(TestCase):
    def setUp(self):
        self.accountOne = Account.objects.create(username="Tweet-Test-1")
        self.accountTwo = Account.objects.create(username="Tweet-Test-2")
        self.testTweet = Tweet.objects.create(
            userID=self.accountOne, message="Created-Test-Tweet")

    def test_post_tweet(self):
        self.assertEqual(createTweet(
            self.accountOne, "Tweet-Test-Post", ""), True)

    def test_view_tweet(self):
        try:
            Tweet.objects.get(message="Created-Test-Tweet")
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_liking_tweet(self):
        likeUserTweet(self.accountTwo, self.testTweet)
        self.assertIn(str(self.testTweet.tweetID),
                      getAllLikedTweets(self.accountTwo))

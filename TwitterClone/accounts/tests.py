from django.test import TestCase
from .models import Account
from django.contrib.auth.models import User
from .views import addUserToDB, followUser, getAllFollowedUsers

# Create your tests here.


class AccountsTestCase(TestCase):
    def setUp(self):
        self.accountOne = Account.objects.create(username="Account-One-User")
        self.accountTwo = Account.objects.create(username="Account-Two-User")

    def test_add_user(self):
        user = User.objects.create_user(
            "Test", "test@test.com", "Thisisatestpassword123")
        addUserToDB(user.username)
        try:
            Account.objects.get(username="Test")
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_follow_user(self):
        followUser(self.accountOne, self.accountTwo)
        followedList = getAllFollowedUsers(self.accountOne)
        self.assertIn(str(self.accountTwo.userID), followedList)

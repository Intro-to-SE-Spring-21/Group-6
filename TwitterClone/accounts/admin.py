from django.contrib import admin
from .models import Account, Following

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('userID', 'username', 'profilePicture')

class FollowingAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following')

admin.site.register(Account, AccountAdmin)
admin.site.register(Following, FollowingAdmin)
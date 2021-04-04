from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Account, Following
# Create your views here.


def loginUser(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request=request, template_name='login.html', context={'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                # return HttpResponseRedirect('/')
                
                
#----------- https://stackoverflow.com/questions/15984700/django-creating-custom-url-for-user-profile
                            username= User.objects.get(username=request.user)

                            url = reverse('Accounts', kwargs = {'username': username.username})
                            return HttpResponseRedirect(url)
#//--------------------------------
            
                        
            else:
                print('User does not exist')
        else:
            return render(request=request, template_name='login.html', context={'form': form})


#----------------------------------        
    url(
    r'^accounts/(?P<username>\w+)/$',
    'pet.views.Accounts',
    name = 'Accounts'
    ),

def Accounts(request, username):
    account = user.objects.get(user = request.user)
    return render(request,'accounts.html',{'account': account, 'tweets': account.getAllPostedTweets(account.userID)})
#//--------------------------------        

    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            passwordPreEncrypt = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=passwordPreEncrypt)
            if user is not None:
                addUserToDB(username)
                login(request, user)
                #return HttpResponseRedirect('/')
             
            
#----------------------------------                   
                            username= User.objects.get(username=request.user)

                            url = reverse('Accounts', kwargs = {'username': username.username})
                            return HttpResponseRedirect(url)
#//--------------------------------        

                
                
            else:
                print('Something went wrong')
    else:
        form = UserCreationForm()
    return render(request=request, template_name='register.html', context={'form': form})


#----------------------------------        
    url(
    r'^accounts/(?P<username>\w+)/$',
    'pet.views.Accounts',
    name = 'Accounts'
    ),
#//--------------------------------        


def logoutUser(request):
    logout(request)
    return redirect('/accounts/login')


def addUserToDB(username):
    newAccount = Account(username=username)
    newAccount.save()
    return True

def currentUserID(request):
    accountReturned = Account.objects.get(username=request.user.username)
    if (accountReturned):
        return accountReturned
    return False

def getAllFollowedUsers(userAccount):
    return list(Following.objects.filter(follower=userAccount).values_list('following', flat=True))

def followUser(followerUser, toFollowUser):
    followerQuerySet = Following.objects.filter(follower = followerUser, following = toFollowUser)
    if followerQuerySet.count() > 0:
        followerQuerySet.delete()
    else:
        followerInstance = Following(follower=followerUser, following=toFollowUser)
        followerInstance.save()

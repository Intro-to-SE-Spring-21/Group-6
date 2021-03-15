from django.shortcuts import render
from django.http import HttpResponse
from tweets.models import tweetForm 
from tweets.views import createTweet, getAllTweets
from accounts.views import currentUserID

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = tweetForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data.items())
                user = currentUserID(request)
                if user:
                    if(createTweet(user, form.cleaned_data["message"], form.cleaned_data["media"])):
                        form = tweetForm
                        pass #if create tweet success
                    else:
                        pass #if create tweet fail

        else:
            form = tweetForm

        tweets = getAllTweets(request)
        
        context = {
            'name': request.user.username,
            'form': form,
            'tweets': tweets,
        }
        return render(request=request, template_name='index.html', context=context)
    else:
        return render(request=request, template_name='unauthenticated.html', context={'name': None})

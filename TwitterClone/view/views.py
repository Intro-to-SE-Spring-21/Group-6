from django.shortcuts import render
from django.http import HttpResponse
from tweets.models import TweetForm 

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='index.html', context={'name': request.user.username})
    else:
        return render(request=request, template_name='unauthenticated.html', context={'name': None})

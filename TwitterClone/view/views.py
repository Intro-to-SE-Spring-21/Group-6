from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='index.html', context={'name': request.user.username})
    else:
        return render(request=request, template_name='index.html', context={'name': None})

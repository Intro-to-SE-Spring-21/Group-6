from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/', views.accountPages, name='user page')
]

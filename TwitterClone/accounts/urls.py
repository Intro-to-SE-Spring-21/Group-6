from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('search/', views.search, name='search'),
    path('<username>/', views.userPageRequest, name="user page"),
]

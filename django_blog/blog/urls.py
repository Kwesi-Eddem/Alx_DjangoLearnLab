from django.urls import path
from . import views
from .views import UserLoginView, register

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
]

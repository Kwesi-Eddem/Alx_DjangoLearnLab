from django.urls import path
from .views import UserLoginView, UserLogoutView, register, profile
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostDeleteView, PostUpdateView
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # Blog post CRUD routes
    path('posts/', PostListView.as_view(), name='posts'),                 # list view
    path('post/new/', PostCreateView.as_view(), name='post-create'),      # create view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # detail view
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # update view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # delete view
]

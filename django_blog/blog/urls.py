from django.urls import path
from .views import UserLoginView, UserLogoutView, register, profile
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostDeleteView, PostUpdateView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    SearchResultsView, PostsByTagView
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


    # Comments (checker-required substrings)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),


    # Tags & search
    path('tags/<str:tag_name>/', PostsByTagView.as_view(), name='posts-by-tag'),
    path('search/', SearchResultsView.as_view(), name='search'),
]

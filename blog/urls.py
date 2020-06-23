from django.conf.urls import url
from django.urls import path
from . import views
from . views import PostListView, PostDetailView, CommentCreate

urlpatterns = [
    path(r'', PostListView.as_view(), name='blog'),
    path(r'post/<int:pk>/', PostDetailView.as_view(), name='post-detail')
]

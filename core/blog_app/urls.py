from django.urls import path
from . import views


app_name = 'blog_app'
urlpatterns = [
    path('posts_list/', views.PostListView.as_view(), name='posts-list'),
]
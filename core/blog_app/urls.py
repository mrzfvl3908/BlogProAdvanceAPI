from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('posts_list/', views.PostListView.as_view(), name='posts-list'),
    path('post_detail/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('create/post/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]

from django.shortcuts import render
from django.views.generic import ListView
from blog_app.models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    paginate_by = 2



from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog_app.models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        key = f'viewed_post_{obj.slug}'

        if not self.request.session.get(key):
            Post.objects.filter(slug=obj.slug).update(
                views=F('views') + 1
            )
            self.request.session[key] = True

        obj.refresh_from_db()
        return obj

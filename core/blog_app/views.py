from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import F
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog_app.forms import PostForm
from blog_app.models import Post


class PostListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    paginate_by = 2


class PostDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    permission_required = 'blog.view_post'

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/posts_list'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/posts_list'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/posts_list/'

from django.shortcuts import render
from django.views.generic import TemplateView
from blog_app.models import Post


class IndexView(TemplateView):
    template_name = 'home_app/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:5]
        return context
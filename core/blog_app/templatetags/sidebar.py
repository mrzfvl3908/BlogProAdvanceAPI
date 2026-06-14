from django import template
from django.db.models import Count, Q
from blog_app.models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('blog_app/includes/recent_posts.html')
def recent_posts():
    rec_posts = Post.objects.filter(status=1)[:3]
    return {'rec_posts': rec_posts}


@register.inclusion_tag('blog_app/includes/post_categories.html')
def post_categories():
    categories = Category.objects.annotate(
        post_count=Count('post', filter=Q(post__status=1))
    ).order_by('-created_date')
    return {'categories': categories}


@register.inclusion_tag('blog_app/includes/post_tags.html')
def post_tags():
    tags = Tag.objects.all()
    return {'tags': tags}

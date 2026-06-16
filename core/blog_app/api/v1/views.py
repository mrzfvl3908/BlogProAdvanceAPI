from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from blog_app.api.v1.serializers import PostSerializer
from blog_app.models import Post


@api_view()
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view()
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

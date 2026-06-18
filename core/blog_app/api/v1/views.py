from django.core.serializers import serialize
from rest_framework import status, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from blog_app.api.v1.serializers import PostSerializer, CategorySerializer
from blog_app.models import Post, Category
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

"""Example DBV"""
# @api_view()
# def post_list(request):
#     posts = Post.objects.filter(status=True).order_by('-created_date')
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)

# @api_view()
# def post_detail(request, id):
#     post = get_object_or_404(Post, pk=id, status=True)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)


"""Example APIView"""
# class PostList(APIView):
#     """
#     getting a list of post and creating new post
#     """
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer #=> برای فرم پست کردن حرفه ای میشه
#
#     def get(self, request):
#         """
#         retrieving a list of posts
#         """
#         posts = Post.objects.filter(status=True)
#         serializer = self.serializer_class(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         """
#         creating a new post
#         """
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class PostDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#
#     def get(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         serializer = self.serializer_class(post, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, id):
#         post = get_object_or_404(Post, pk=id, status=True)
#         post.delete()
#         return Response({"detail": "successfully delete post"}, status=status.HTTP_204_NO_CONTENT)


"""Example GenericView"""
# class PostList(ListCreateAPIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)


"""Example ModelViewSet"""
class PostListModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'author', 'status']

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

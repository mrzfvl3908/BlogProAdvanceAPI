from rest_framework import serializers
from blog_app.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'category', 'author', 'title', 'content', 'image', 'status', 'created_date']
        # read_only_fields = ['content']

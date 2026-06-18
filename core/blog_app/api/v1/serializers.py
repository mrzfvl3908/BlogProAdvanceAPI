from rest_framework import serializers
from blog_app.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'category', 'author', 'title', 'content', 'snippet', 'image', 'status', 'created_date',
                  'relative_url']
        # read_only_fields = ['content']

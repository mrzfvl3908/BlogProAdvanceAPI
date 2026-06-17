from rest_framework import serializers
from blog_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','category','author','title','content','image','status','created_date']

from django.template.context_processors import request
from rest_framework import serializers
from blog_app.models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')  # => توابع وابسته به مدل و فانکشن از مدل
    relative_url = serializers.URLField(source='get_absolute_api_url',
                                        read_only=True)  # => توابع وابسته به مدل و فانکشن از مدل
    absolute_url = serializers.SerializerMethodField()  # => برای توابه ئابسته بع داخل سریالایزر اگه درخواست داریم باید از درو همین سریالایزر فانکشن بنویسم اگر ن از مدل میشه
    # absolute_url = serializers.SerializerMethodField(method_name='get_abs_url') => get_absolute_url برای تغییر نام و استفاده از متد نام به جای
    # category = CategorySerializer() => گرفتن موارد کتگوری

    class Meta:
        model = Post
        fields = ['id', 'category', 'author', 'title', 'content', 'snippet', 'image', 'status', 'created_date',
                  'relative_url', 'absolute_url']
        # read_only_fields = ['content']

    def get_absolute_url(self, obj): #=> برای توابع درونی سریالایزر
        request = self.context.get('request')
        return request.build_absolute_uri(
            obj.get_absolute_api_url()
        )

    def to_representation(self, instance):
        return super().to_representation(instance)

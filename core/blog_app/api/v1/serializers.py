from rest_framework import serializers
from accounts_app.models import Profile
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
        read_only_fields = ['author']

    def get_absolute_url(self, obj):  # => برای توابع درونی سریالایزر
        request = self.context.get('request')
        return request.build_absolute_uri(
            obj.get_absolute_api_url()
        )

    def to_representation(self, instance):  # => برای گرفتن ابجکت و حذف در post_detail و نمایش در لیست پست ها
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)

        rep['category'] = CategorySerializer(instance.category, context={request: 'request'}).data
        return rep

    def create(self, validated_data):  # => برای اینکه در هنگام ایجاد پست کاربری که لاگین شده با همون کاربر پست ثبت بشه
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)

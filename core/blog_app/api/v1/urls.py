from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'api-v1'

router = DefaultRouter()

router.register('post', views.PostListModelViewSet, basename='post')

urlpatterns = router.urls




# urlpatterns = [
#     path('post/', views.PostList.as_view(), name='post-list'),
#     path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
# ]

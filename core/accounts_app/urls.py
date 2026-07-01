from django.urls import path, include
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

app_name = "accounts_app"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path('api/v1/', include('accounts_app.api.v1.urls')),
]
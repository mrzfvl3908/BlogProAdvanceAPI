from django.urls import path
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

app_name = "accounts_app"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterPage.as_view(), name="register"),

    # logout
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
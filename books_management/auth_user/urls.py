from django.contrib import admin
from django.urls import path,include
from auth_user.views import login_user,register_user,logout_view

urlpatterns = [
    path("register/",register_user,name="register_user"),
    path("login/",login_user,name="login_user"),
    path("logout/",logout_view,name="logout_view"),
]

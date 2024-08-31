from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout", views.signout, name="logout"),
    path("post/<slug:slug>/", views.post_detail, name="post"),
    path("post/new", views.posting, name="new-post"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("search", views.PostSearch, name="search"),
]

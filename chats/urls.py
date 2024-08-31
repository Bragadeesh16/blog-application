from django.urls import path
from . import views

urlpatterns = [
    path("search-user", views.SearchUsers, name="search_user"),
    path("user-profile/<int:pk>", views.UserProfile, name="user-profile"),
    path("send-request", views.send_friend_request, name="send-request"),
    path("notification", views.notifications, name="notifications"),
    path("adding_friend", views.adding_friend, name="adding-friend"),
    path("personal-chat/<int:pk>", views.PersonalChat, name="personal-chat"),
]

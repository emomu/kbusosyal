from django.urls import path
from .views import logoutt, profile_list , profile , kesfet , like_post , follows_list , followed_list , dashboardposted , loginn , register , giris , profile_list_query

app_name = "dwitter"

urlpatterns = [
    path("profile_list/", profile_list , name="profile_list"),
    path("", giris , name="giris"),
    path("profile/<int:pk>", profile , name="profile"),
    path("kesfet/", kesfet , name="kesfet"),
    path("like/", like_post , name="like-post"),
    path("follows/<int:pk>", follows_list , name="follows-list"),
    path("followed/<int:pk>", followed_list , name="followed-list"),
    path("yurtlar/", dashboardposted , name="yurtlar"),
    path("login/", loginn , name="login"),
    path("logout/", logoutt , name="logout"),
    path("register/", register , name="register"),
    path("aramasonucu/", profile_list_query , name="aramasonucu"),


]
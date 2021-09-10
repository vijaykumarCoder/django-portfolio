from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("posts/",posts,name="posts"),
    path("post/",post,name="post"),
    path("profile/",profile,name="profile"),
    path("uploadImage/",uploadImage,name="uploadImage"),
    path("post_form/", postForm, name="postForm"),
    path("updatePost/<str:pk>",updatePost, name="updatePost"),
    path("delete/<str:id>", deletePost,name="delete"),
    path("pagenator/", pagePage, name="pagePage"),
]

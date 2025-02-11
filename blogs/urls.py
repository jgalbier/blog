"""Defines URL patterns for blogs."""

from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path("", views.home, name="home"),
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/<int:blog_id>/", views.blog_post, name="blog_post"),
    path("new_blog/", views.new_blog, name="new_blog"),
    path("new_post/<int:blog_id>/", views.new_post, name="new_post"),
    path("edit_post/<int:blog_id>/<int:post_id>/", views.edit_post, name="edit_post"),
    path("delete_post/<int:blog_id>/<int:post_id>/", views.delete_post, name="delete_post"),
]
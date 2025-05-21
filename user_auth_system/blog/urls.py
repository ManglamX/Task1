from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    path('create/', views.create_post, name='create_post'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
] 
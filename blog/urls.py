from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts, name='blog'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),
]

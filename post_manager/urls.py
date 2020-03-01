from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "post"


urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('view/<int:pk>/', views.PostDetailView.as_view(), name='view'),
    path('comment_delete/<int:pk>/', views.comment_delete, name='comment_delete'),
]

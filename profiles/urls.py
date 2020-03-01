from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "profile"


urlpatterns = [
    path('<username>', views.profile_view, name='index'),
    path('all/', views.ProfileListView.as_view(), name='all' )
]

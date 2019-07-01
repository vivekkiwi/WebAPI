from django.conf.urls import url
from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.FeedItemList.as_view()),
]

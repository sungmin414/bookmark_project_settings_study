from django.urls import path
from django.views.generic import ListView, DetailView

from .models import Bookmark
from . import views

app_name = 'bookmark'

urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    # path('', ListView.as_view(model=Bookmark), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    # path('<int:pk>/', DetailView.as_view(model=Bookmark), name='detail')
]
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Bookmark


# list_view
class BookmarkLV(ListView):
    model = Bookmark


# detail_view
class BookmarkDV(DetailView):
    model = Bookmark


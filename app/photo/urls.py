from django.urls import path

from photo.models import Album
from photo.views import *

app_name = 'photo'

urlpatterns = [
    path('', AlbumLV.as_view(), name='index'),
    path('album/', AlbumLV.as_view(), name='album_list'),
    path('album/<int:pk>/', AlbumDV.as_view(), name='album_detail'),
    path('photo/<int:pk>/', PhotoDV.as_view(), name='photo_detail'),

]

#   path('', ListView.as_view(model=Album), name='index') 이런식으로 하면 views 코딩 안해도 된다.
#   path('', DetailView.as_view(model=Album), name='album_detail') 이런식으로 하면 views 코딩 안해도 된다.

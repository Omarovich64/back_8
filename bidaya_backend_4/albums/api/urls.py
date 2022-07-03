from django.urls import path, include
from albums.api.views import AlbumList, AlbumDetail, AlbumCreate




urlpatterns = [

    path('create-album/', AlbumCreate.as_view(), name='album-create'),
    path('list-albums/', AlbumList.as_view(), name='album-list'),
    path('detail/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),

]


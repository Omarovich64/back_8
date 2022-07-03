from django.contrib import admin
from albums.models import Album, AlbumImage

# Register your models here.

admin.site.register(Album)
admin.site.register(AlbumImage)

from rest_framework import serializers
from albums.models import Album, AlbumImage






class AlbumImageSerializer(serializers.ModelSerializer):
    album = serializers.StringRelatedField()

    class Meta:
        model = AlbumImage
        fields = "__all__"


class AlbumsSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    images = AlbumImageSerializer(read_only = True, many = True)

    class Meta:
        model = Album
        fields = ('id', 'owner', 'title', 'images')

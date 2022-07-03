from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


def upload_path(instance, filname):
    return '/'.join(['covers', str(instance.title), filname])


def upload_path_2(instance, filname):
    return '/'.join(['images', filname])


class Album(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    cover_photo = models.ImageField(
        blank=True, null=True, upload_to=upload_path, default="fondGris.jpg")

    def __str__(self):
        return self.title


class AlbumImage(models.Model):

    image_url = models.ImageField(
        blank=True, null=True, upload_to=upload_path_2)
    title = models.CharField(max_length=30)
    album = models.ForeignKey(
        Album, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Generated by Django 3.2.5 on 2022-06-16 17:36

import albums.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0013_auto_20220613_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='album',
            name='image',
        ),
        migrations.RemoveField(
            model_name='album',
            name='photos_number',
        ),
        migrations.AddField(
            model_name='album',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=albums.models.upload_path),
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=albums.models.upload_path_2)),
                ('title', models.CharField(max_length=30)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.album')),
            ],
        ),
    ]

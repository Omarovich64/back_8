# Generated by Django 3.2.5 on 2022-05-22 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Albums',
            new_name='Album',
        ),
    ]
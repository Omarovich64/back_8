# Generated by Django 3.2.5 on 2022-05-22 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('cover', models.IntegerField(default=0)),
                ('photos_number', models.IntegerField(default=0)),
            ],
        ),
    ]

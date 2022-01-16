# Generated by Django 3.2.8 on 2022-01-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0025_auto_20220115_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_article',
            name='category2',
        ),
        migrations.RemoveField(
            model_name='movie_article',
            name='category3',
        ),
        migrations.AddField(
            model_name='movie_article',
            name='size_1080p',
            field=models.CharField(default='download 1080p', max_length=20),
        ),
        migrations.AddField(
            model_name='movie_article',
            name='size_2160p',
            field=models.CharField(default='download 2160p', max_length=20),
        ),
        migrations.AddField(
            model_name='movie_article',
            name='size_720p',
            field=models.CharField(default='download 720p', max_length=20),
        ),
    ]

# Generated by Django 3.2.8 on 2022-01-16 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0023_alter_movie_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_article',
            name='category',
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0007_alter_movie_article_synopsis'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_article',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2023-01-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0076_remove_movie_article_download_2160p_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_article',
            name='director',
            field=models.CharField(default='...', max_length=50),
        ),
    ]

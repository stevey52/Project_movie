# Generated by Django 3.2.8 on 2022-01-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0026_auto_20220116_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_article',
            name='size_1080p',
            field=models.CharField(default='1080p', max_length=200),
        ),
        migrations.AlterField(
            model_name='movie_article',
            name='size_2160p',
            field=models.CharField(default='2160p', max_length=200),
        ),
        migrations.AlterField(
            model_name='movie_article',
            name='size_720p',
            field=models.CharField(default='720p', max_length=200),
        ),
    ]

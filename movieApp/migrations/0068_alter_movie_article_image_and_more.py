# Generated by Django 4.0.4 on 2022-12-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0067_alter_movie_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_article',
            name='image',
            field=models.ImageField(blank=True, default='logos.jpeg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie_article',
            name='image_bg',
            field=models.ImageField(default='movieApp/cinema2.jpg', upload_to=''),
        ),
    ]
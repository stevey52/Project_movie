# Generated by Django 4.0.4 on 2022-12-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0061_movie_article_image_bg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_article',
            name='image_bg',
            field=models.ImageField(blank=True, default='cinema.jpg', upload_to=''),
        ),
    ]
# Generated by Django 3.2.8 on 2022-12-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0037_auto_20221210_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_article',
            name='image_bg',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

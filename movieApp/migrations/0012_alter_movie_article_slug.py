# Generated by Django 3.2.7 on 2021-09-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0011_auto_20210914_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_article',
            name='slug',
            field=models.SlugField(default=3, unique=True),
            preserve_default=False,
        ),
    ]

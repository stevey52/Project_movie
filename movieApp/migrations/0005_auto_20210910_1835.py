# Generated by Django 3.2.7 on 2021-09-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0004_auto_20210910_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie_article',
            name='slug',
        ),
        migrations.AddField(
            model_name='movie_article',
            name='synopsis',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

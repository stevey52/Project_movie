# Generated by Django 4.0.4 on 2022-04-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0055_auto_20220208_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream_movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('Movie', models.FileField(upload_to='')),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2023-06-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0048_blogs_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

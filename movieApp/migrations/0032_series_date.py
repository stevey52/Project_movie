# Generated by Django 3.2.8 on 2022-01-23 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0031_remove_series_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

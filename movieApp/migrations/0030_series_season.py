# Generated by Django 3.2.8 on 2022-01-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0029_tv_series_production'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='season',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

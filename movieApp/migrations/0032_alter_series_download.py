# Generated by Django 3.2.8 on 2022-01-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0031_alter_series_download'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='download',
            field=models.CharField(default='...', max_length=200),
        ),
    ]
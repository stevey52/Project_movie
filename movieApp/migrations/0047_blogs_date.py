# Generated by Django 4.0.4 on 2023-06-17 11:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0046_delete_tv_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

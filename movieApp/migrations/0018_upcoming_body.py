# Generated by Django 3.2.7 on 2021-10-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0017_remove_upcoming_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcoming',
            name='body',
            field=models.TextField(null=True),
        ),
    ]

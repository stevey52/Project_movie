# Generated by Django 4.0.4 on 2022-11-08 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0057_slidesmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slidesmodel',
            old_name='name',
            new_name='title',
        ),
    ]

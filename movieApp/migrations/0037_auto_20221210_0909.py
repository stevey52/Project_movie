# Generated by Django 3.2.8 on 2022-12-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0036_alter_movie_article_genre3'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlidesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ratings', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(blank=True, default='logos.jpeg', upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie_article',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie_article',
            name='director_info',
        ),
        migrations.RemoveField(
            model_name='movie_article',
            name='size_1080p',
        ),
        migrations.RemoveField(
            model_name='movie_article',
            name='size_2160p',
        ),
        migrations.RemoveField(
            model_name='movie_article',
            name='size_720p',
        ),
        migrations.RemoveField(
            model_name='series',
            name='date',
        ),
        migrations.AddField(
            model_name='movie_article',
            name='duration',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='movie_article',
            name='image_bg',
            field=models.ImageField(blank=True, default='static/images/cinema.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='series',
            name='image_bg',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie_article',
            name='category',
            field=models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('horror', 'Horror'), ('animated', 'Animation'), ('drama', 'Drama')], default='horror', max_length=200),
        ),
        migrations.AlterField(
            model_name='movie_article',
            name='genre3',
            field=models.CharField(default='...', max_length=50),
        ),
        migrations.AlterField(
            model_name='tv_series',
            name='production',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

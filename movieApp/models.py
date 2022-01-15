from django.db import models
import datetime
from django.urls import reverse
from django.utils.timezone import now

#year selection for movie_article
YEAR_CHOICES = []
for r in range(1940, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

#year selection for old is gold
CHOOSE_YEAR = []
for y in range(1940, (datetime.datetime.now().year+1)):
    CHOOSE_YEAR.append((y,y))

category_choices = (
    ('action','Action'),
    ('comedy', 'Comedy'),
    ('horror', 'Horror'),
    ('animated', 'Animation'),
)

# Create your models here.
class Movie_article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    synopsis = models.CharField(max_length=50,default="Synopsis")
    ratings = models.CharField(max_length=50,null=True)
    genre1 = models.CharField(max_length=50,null=True)
    genre2 = models.CharField(max_length=50,null=True)
    genre3 = models.CharField(max_length=50,default="...")
    year = models.IntegerField(('year'),choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    download_720p = models.CharField(max_length=200,null=True)
    download_1080p = models.CharField(max_length=200,null=True)
    download_2160p = models.CharField(max_length=200,null=True)
    trailer = models.CharField(max_length=200,null=True)
    director = models.CharField(max_length=50,default="...")
    director_info = models.CharField(max_length=500,null=True)
    category = models.CharField(max_length=200, default="horror", choices=category_choices)
    body = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='logos.jpeg',blank=True)
    #add author



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailView', kwargs={'slug': self.slug})

#preview only first 50 characters of the body
    def snippest(self):
        return self.body[:200] + "..."




class Upcoming(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True, default="upcoming")
    synopsis = models.CharField(max_length=200, default="Synopsis")
    genre1 = models.CharField(max_length=50,null=True)
    genre2 = models.CharField(max_length=50,null=True)
    genre3 = models.CharField(max_length=50,default="...")
    trailer = models.CharField(max_length=200,null=True)
    image = models.ImageField(default='logos.jpeg',blank=True)
    date = models.DateTimeField(auto_now_add=True)
    release_Date = models.DateField(u'Release Date') #calendar for date picker
    body = models.TextField(null=True)



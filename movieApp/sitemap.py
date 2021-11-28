from django.contrib.sitemaps import Sitemap
from .models import Movie_article  #post class from models

class Movie_articleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Movie_article.objects.all()

    def lastmodified(self, obj):
        return obj.date   #updated == date posted

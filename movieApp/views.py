from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.
class HomePage(ListView):
    model = Movie_article
    template_name = "homeView.html"
    ordering = ['-date']  #odering posts by date, last posted to be new post

class DetailsPage(DetailView):
    model = Movie_article
    template_name = "detailView.html"

class UpcomingMovies(ListView):
    model = Upcoming
    template_name = "upcoming.html"
    ordering = ['-date']

class Upcoming_details(DetailView):
    model = Upcoming
    template_name = "upcomingDetail.html"

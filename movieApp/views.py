from django.shortcuts import render
from django.views.generic import *
from django.db.models import Q # new
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


class SearchResultsView(ListView):
    template_name = 'homeView.html'
    model = Movie_article


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)

        else:
            object_list = self.model.objects.none()

        return object_list

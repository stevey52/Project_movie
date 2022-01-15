from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

urlpatterns = [
# slug added to capture name from SlugField to url
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),

    path("action/",Action.as_view(), name="action_movies"),
   
    path("contact-us/",sendMail, name='contact_us'),

    path("about_movie/<slug>/",ReadMore.as_view(),name="read_more"),

    path('search-movie/',SearchResultsView.as_view(), name='search_results'),

    path("Upcoming/<slug>/",Upcoming_details.as_view(), name="upcomingDetail"),
    path("Upcoming/",UpcomingMovies.as_view(), name="upcoming"),
    path("Movie_article/<slug>/",DetailsPage.as_view(), name="detailView"),
    path("",HomePage.as_view(), name="homeView")
]

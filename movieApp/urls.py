from django.urls import path
from .views import *

urlpatterns = [
# slug added to capture name from SlugField to url
    path("old-is-gold/",Old_Gold, name='old_is_gold'),
    path("contact-us/",sendMail, name='contact_us'),
    path("about-movie/",ReadMore.as_view(),name="read_more"),
    path('search-movie/',SearchResultsView.as_view(), name='search_results'),
    path("Upcoming/<slug>/",Upcoming_details.as_view(), name="upcomingDetail"),
    path("Upcoming/",UpcomingMovies.as_view(), name="upcoming"),
    path("Movie_article/<slug>/",DetailsPage.as_view(), name="detailView"),
    path("",HomePage.as_view(), name="homeView")
]

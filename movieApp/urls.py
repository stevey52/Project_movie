from django.urls import path
from .views import *

urlpatterns = [
# slug added to capture name from SlugField to url
    path("Upcoming/<slug>/",Upcoming_details.as_view(), name="upcomingDetail"),
    path("Upcoming/",UpcomingMovies.as_view(), name="upcoming"),
    path("Movie_article/<slug>/",DetailsPage.as_view(), name="detailView"),
    path("",HomePage.as_view(), name="homeView")
]

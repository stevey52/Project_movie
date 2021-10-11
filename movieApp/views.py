from django.shortcuts import render
from django.views.generic import *
from django.core.paginator import Paginator #importing module for breaking pages
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
# from django.template import Template, Context
# from django.template.loader import render_to_string

# Create your views here.
class HomePage(ListView):
    model = Movie_article
    template_name = "homeView.html"
    paginate_by = 12  #diving pages contents(each page to have 12 contents)
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

#search functionality buy quering the database from user inputs
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

class ReadMore(TemplateView):
    model = Movie_article
    template_name = "readMore.html"

    def read_more(request):

        rendered = render_to_string('readMore.html', {'foo': 'bar'})
        response = HttpResponse(rendered)

        return response

class ContactUs(TemplateView):
    template_name = "contact.html"


    def contact(request):
        name = request.GET.get["users_name", '']
        email = request.GET.get["users_email", '']
        sent_message = request.GET.get["message",'']
        # send = request.GET.get["message",'']

        if name and email and sent_message:
            try:
                # send Email
                send_mail(
                email,
                name,
                sent_message,
                [""],
                )

            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')

            return HttpResponseRedirect('/contact/thanks')

        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')

            # return render(request, "contact.html",{"name":name})
        # else:
            # return render(request, "contact.html", {})

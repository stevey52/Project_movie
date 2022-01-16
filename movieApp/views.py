
from unicodedata import category
from django.shortcuts import render
from django.views.generic import *
from django.core.paginator import Paginator #importing module for breaking pages
from .models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from.forms import EmailForm
from django.conf import settings
import os
import environ
# from django.template import Template, Context
# from django.template.loader import render_to_string

# Create your views here.
class HomePage(ListView):
    model = Movie_article
    template_name = "homeView.html"
    paginate_by = 14  #divide pages contents(each page to have 12 contents)
    ordering = ['-date']  #odering posts by date, last posted to be new post


class DetailsPage(DetailView):
    model = Movie_article
    template_name = "detailView.html"

class UpcomingMovies(ListView):
    model = Upcoming
    template_name = "upcoming.html"
    ordering = ['-date']
    paginate_by = 14

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

class ReadMore(DetailView):
    model = Movie_article
    template_name = "readMore.html"



# Sending an Email

def sendMail(request):

    #create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':
        form = EmailForm(request.POST)
        sender = request.POST['sender']
        senderEmail = request.POST['sender_email']

        # check if data from form is clean

        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sender " + sender
            message = cd['message']

            message1 = message + "\n" + senderEmail

            # send the email to the recipient

            send_mail(subject, message1,
                    settings.DEFAULT_FROM_EMAIL, [os.environ.get('FROM_EMAIL')])

            # set the variable initially created to True

            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'contact.html', {

        'form':form,
        'messageSent':messageSent,

    })


#Views for action movies category
class Action(ListView):
    model = Movie_article
    template_name = "homeView.html"


    def get_queryset(self):
        
        object_list = self.model.objects.filter(category="action")
            

        return object_list


#Views for comedy movies category
class Comedy(ListView):
    model = Movie_article
    template_name = "homeView.html"


    def get_queryset(self):
        
        object_list = self.model.objects.filter(category__in=["comedy","drama"])


        return object_list




#Views for animated movies category
class Animation(ListView):
    model = Movie_article
    template_name = "homeView.html"


    def get_queryset(self):
        
        object_list = self.model.objects.filter(category="animated")

        return object_list




#Views for Horror movies category
class Horror(ListView):
    model = Movie_article
    template_name = "homeView.html"


    def get_queryset(self):
        
        object_list = self.model.objects.filter(category="horror")

        return object_list

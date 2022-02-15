from cProfile import label
from django import forms

from movieApp.models import Movie_article, Series

class EmailForm(forms.Form):
    sender = forms.CharField(max_length=20,label='Name')
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    # styling django forms with django css styling
    sender.widget.attrs.update(
        {'class':'form-control','placeholder':'Your Name', 'required':'required'}
    )
    sender_email.widget.attrs.update(
        {'class':'form-control','placeholder':'Your Email', 'required':'required'})

    message.widget.attrs.update(
        {'class':'form-control','placeholder':'Type your Message:', 'required':'required'})



class SearchField(forms.Form):
    movie_search = forms.CharField(max_length=50, label="Search")



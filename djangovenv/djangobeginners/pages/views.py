from django.http import HttpResponse
from django.shortcuts import render

# To find a url to a specific view, django will look in the main configuration file set up by default (project root/settings.py) in ROOT_URLCONF. Then, with a matching url,
# django will look for a matching view that is made to handle that url. 
# Create your views here.
# *args is a tuple of arguments passed into a function
# **kwargs is a dictionary of arguments passed into a function
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>") # Hello World Will be rendered in the browser as an HTML string as a header 

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact page</h1>") 
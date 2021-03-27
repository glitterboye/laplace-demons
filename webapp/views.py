from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# home method accepts a request
def home(request):
    return HttpResponse("Welcome! You are now looking at the views DOT home page.")


# Can I put a second function here?
def nest(request):
    return HttpResponse("It seems like you have now entered views DOT nest. Enjoy your stay!")

from django.http import HttpResponse


# home method accepts a request
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name':'User'}) # rendering dynamic content

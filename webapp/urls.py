from django.urls import path

from . import views

# List of possible URL Patterns
urlpatterns = [
    path('', views.home, name='home'), # views.index is calling fxn

    # TODO add another possible path
]
from django.shortcuts import render
from django.conf import settings

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view to return the index page """

    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY
    }

    return render(request, 'home/contact.html', context)

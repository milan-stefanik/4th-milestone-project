from django.http import HttpResponse


def index(request):
    return HttpResponse('<p>Hello, world. You are at the lms index.</p>')

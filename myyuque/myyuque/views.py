from django.http import HttpResponse


def hello(self):
    return HttpResponse("Hello word!")
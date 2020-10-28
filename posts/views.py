from django.shortcuts import render

# Create your views here.


def index(request):
    """ A Views to return the index page """
    return render(request, "posts/index.html")

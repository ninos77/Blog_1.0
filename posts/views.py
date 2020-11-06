from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.


class IndexView(ListView):
    """ A Views to return the index page """
    template_name = "posts/posts.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

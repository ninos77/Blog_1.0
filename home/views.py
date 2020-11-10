from django.shortcuts import render
from posts.models import Post
from django.views.generic import ListView
# Create your views here.


class IndexView(ListView):
    template_name = "home/index.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-publishing_date')
        return context

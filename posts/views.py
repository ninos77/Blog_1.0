from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.


class AllBlog(ListView):
    template_name = "posts/all_blog.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-publishing_date')
        return context

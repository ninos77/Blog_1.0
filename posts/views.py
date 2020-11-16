from django.shortcuts import get_object_or_404, render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView
# Create your views here.


class AllBlog(ListView):
    template_name = "posts/all_blog.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-publishing_date')
        return context


class BlogDetail(DetailView):
    template_name = "posts/single_post.html"
    model = Post
    context_object_name = 'blog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        return context


class Category_blog(ListView):
    template_name = "posts/category_blog.html"
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category).order_by("-id")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Category_blog, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        context['category'] = self.category
        return context


class TagDetails(ListView):
    template_name = "posts/tag_detail.html"
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Post.objects.filter(tag=self.tag).order_by("id")

    def get_context_data(self, **kwargs):
        context = super(TagDetails, self).get_context_data(**kwargs)
        self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        context['tag'] = self.tag
        return context

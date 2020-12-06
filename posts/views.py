from django.shortcuts import get_object_or_404, render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import PostCreationForm, PostUpdateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.http import HttpResponseRedirect
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


@method_decorator(login_required(login_url='users/login'), name='dispatch')
class PostCreateView(CreateView):
    template_name = 'posts/create_post.html'
    form_class = PostCreationForm
    model = Post

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()

        tags = self.request.POST.get('tag').split(',')

        for tag in tags:
            curent_tag = Tag.objects.filter(slug=slugify(tag))
            if curent_tag.count() < 1:
                create_tag = Tag.objects.create(title=tag)
                form.instance.tag.add(create_tag)
            else:
                existed_tag = Tag.objects.get(slug=slugify(tag))
                form.instance.tag.add(existed_tag)
        return super(PostCreateView, self).form_valid(form)


@method_decorator(login_required(login_url='users/login'), name='dispatch')
class UpdatePostView(UpdateView):
    template_name = "posts/post_update.html"
    model = Post
    form_class = PostUpdateForm

    def get_success_url(self):
        return reverse('post_update', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.tag.clear()

        tags = self.request.POST.get('tag').split(',')

        for tag in tags:
            curent_tag = Tag.objects.filter(slug=slugify(tag))
            if curent_tag.count() < 1:
                create_tag = Tag.objects.create(title=tag)
                form.instance.tag.add(create_tag)
            else:
                existed_tag = Tag.objects.get(slug=slugify(tag))
                form.instance.tag.add(existed_tag)
        return super(UpdatePostView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.user != request.user:
            return HttpResponseRedirect('/')
        return super(UpdatePostView, self).get(request, *args, **kwargs)

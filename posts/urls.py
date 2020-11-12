from django.urls import path
from .views import *


urlpatterns = [
    path('blogs/', AllBlog.as_view(), name='all_blogs'),
    path('detail/<int:pk>/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),
    path('category_blog/<int:pk>/<slug:slug>',
         Category_blog.as_view(), name='category_blog')


]

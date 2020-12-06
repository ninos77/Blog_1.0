from django.urls import path
from .views import *


urlpatterns = [
    path('blogs/', AllBlog.as_view(), name='all_blogs'),
    path('detail/<int:pk>/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),
    path('post_update/<int:pk>/<slug:slug>',
         UpdatePostView.as_view(), name='post_update'),
    path('category_blog/<int:pk>/<slug:slug>',
         Category_blog.as_view(), name='category_blog'),
    path('tag/<int:pk>/<slug:slug>', TagDetails.as_view(), name='tag_detail'),
    path('create_post', PostCreateView.as_view(), name='create_post')
]

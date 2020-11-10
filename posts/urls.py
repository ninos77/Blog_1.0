from django.urls import path
from .views import *


urlpatterns = [
    path('blogs/', AllBlog.as_view(), name='all_blogs'),
    path('detail/<int:pk>/<slug:slug>', BlogDetail.as_view(), name='blog_detail')

]

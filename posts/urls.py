from django.urls import path
from .views import *


urlpatterns = [
    path('', AllBlog.as_view(), name='all_blogs')

]

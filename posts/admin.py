from django.contrib import admin
from .models import Post


class AdminPost(admin.ModelAdmin):
    list_filter = ['publishing_date']
    list_display = ['title', 'user', 'publishing_date']
    search_fields = ['title', 'content']

    class Meta:
        model = Post


admin.site.register(Post, AdminPost)

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=150)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    slug = models.SlugField(default="slug")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_first_word(self):
        return self.title.partition(' ')[0]

    def get_rest_title(self):
        return self.title.split(' ', 1)[1]

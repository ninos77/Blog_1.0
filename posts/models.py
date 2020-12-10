from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=150)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def blog_count(self):
        return self.blogs.all().count()


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

    def blog_count(self):
        return self.blogs.all().count()


class Post(models.Model):

    title = models.CharField(max_length=150)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category, default=1,
                                 on_delete=models.CASCADE, related_name="blogs")
    slug = models.SlugField(default="slug", editable=False)
    tag = models.ManyToManyField(Tag, related_name="blogs", blank=True)
    hit = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_first_word(self):
        return self.title.partition(' ')[0]

    def get_rest_title(self):
        return self.title.split(' ', 1)[1]

    def __str__(self):
        return self.title

    def post_tag(self):
        return ','.join(str(tag) for tag in self.tag.all())

    def post_count(self):
        return Post.objects.all().count()

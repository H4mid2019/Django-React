from django.db import models
from django.utils import timezone

# Create your models here.


class Writer(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    position = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=40, blank=True, null=True)
    tags = models.CharField(max_length=40, blank=True, null=True)
    slug = models.SlugField(null=True,
                            allow_unicode=True, unique=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    brief = models.TextField(max_length=185)
    article = models.TextField(max_length=9000000, blank=True, null=True)
    imag = models.ImageField(upload_to='blog_image/', blank=True, null=True)
    # date_added = models.DateField(default=timezone.now, blank=True, null=True)
    ff = models.ForeignKey(
        Writer, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def taglist(self):
        return self.tags.split('-')

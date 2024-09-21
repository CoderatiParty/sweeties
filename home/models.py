from django.db import models
from django.utils import timezone


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Article(models.Model):
    category = models.ForeignKey('Category', null=True, blank=False,
                                 on_delete=models.SET_NULL)
    sub_category = models.CharField(max_length=254, null=False, blank=False)
    headline = models.CharField(max_length=1024, null=False, blank=False)
    article_text = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)
    image_description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.headline
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
    Model for categories.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Article(models.Model):
    """
    Model for news article info
    """
    category = models.ForeignKey('Category', null=True, blank=False,
                                 on_delete=models.SET_NULL)
    sub_category = models.CharField(max_length=254, null=False, blank=False)
    headline = models.CharField(max_length=1024, null=False, blank=False, db_index=True)
    article_text = models.TextField(null=True, blank=True, db_index=True)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(null=True, blank=True)
    image_name = models.CharField(max_length=254, null=False, blank=False)
    image_description = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.headline
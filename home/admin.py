from django.contrib import admin
from .models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sub_category',
        'headline',
        'article_text',
        'date',
        'image',
        'image_description',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
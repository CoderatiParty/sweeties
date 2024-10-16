from django import forms
from .models import Category, Article
from django.shortcuts import get_object_or_404


class AddArticleForm(forms.ModelForm):
    """
    Function for adding/editing articles
    """
    class Meta:
        model = Article
        fields = ('category', 'sub_category', 'headline', 'article_text', 'date', 'image', 'image_name', 'image_description',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'category': 'Category',
            'sub_category': 'Sub-category',
            'headline': 'Headline',
            'article_text': 'Article Text',
            'date': 'Date',
            'image': 'Image',
            'image_name': 'Image Name',
            'image_description': 'Image Description',
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders.get(field, field.capitalize())} *'
                else:
                    placeholder = placeholders.get(field, field.capitalize())
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False

    def save(self, commit=True, user=None):
        """ Ensure user is passed to the form when saving """
        article = super().save(commit=False)
        if commit:
            article.save()
        return article
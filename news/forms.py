from django import forms
from django_filters import ModelChoiceFilter

from .models import Post, PostCategory, Category


class PostForm(forms.ModelForm):



    class Meta:

        model = Post

        fields = ['posts', 'author', 'choice_title', 'title', 'post_text', ]

class PostCategoryForm(forms.ModelForm):

    class Meta:
        model = Post
        posts = ModelChoiceFilter(choices=Category.POSITION)

        fields = {'posts': ['exact']}
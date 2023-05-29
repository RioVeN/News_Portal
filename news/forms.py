from django import forms
from django.forms import ModelChoiceField

from .models import Post, PostCategory, Category, Author


class PostForm(forms.ModelForm):


    class Meta:

        model = Post

        fields = ['posts', 'author', 'title', 'post_text']


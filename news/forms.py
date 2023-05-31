from django import forms
from django.forms import ModelChoiceField

from .models import Post, PostCategory, Category, Author

from django import forms


class PostForm(forms.ModelForm):
    # posts = forms.ModelChoiceField(label= 'Категория', queryset=Category.objects.all())
    # author = forms.ModelChoiceField(label= 'Автор', queryset=Author.objects.all())
    # title =  forms.Field(label='Заголовок')
    class Meta:

        model = Post

        fields = ['posts', 'author', 'title', 'post_text']


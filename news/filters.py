from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, Author, PostCategory


class PostFilter(FilterSet):
    #author = ModelChoiceFilter(field_name='author', queryset=Author.objects.all(), label='Author', empty_label='любой')
    #posts = ModelChoiceFilter(field_name='posts', queryset=PostCategory.objects.all(), label='Category', empty_label='любой' )
    class Meta:
        model = Post
        fields = {
            #'posts': ['exact'],
            'title': ['icontains'],
            'author':['exact'],
            'time_in_comment': [
               'gt',
            ],
        }
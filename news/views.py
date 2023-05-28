from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .forms import PostForm, PostCategoryForm
from .models import Post
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-time_in_comment'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10



class PostDetail(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = "news"


class PostSearch(ListView):
    model = Post
    ordering = '-time_in_comment'
    template_name = 'news_search.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
def create_post(request):
    form = PostForm()
    form2 = PostCategoryForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect('/news/')

    return render(request, 'post_edit.html', {'form': form, 'form2': form2})

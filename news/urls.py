from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostSearch, create_post

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', PostSearch.as_view()),
   path('create/', create_post, name='post_create')
]

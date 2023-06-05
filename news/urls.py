from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostSearch, PostCreate, ArticleCreate, PostUpdate, PostDelete, upgrade_me
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),

    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/search/', PostSearch.as_view()),
    path('news/create/', PostCreate.as_view(),  name='post_create'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('upgrade/', upgrade_me, name='upgrade')

]

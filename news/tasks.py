from celery import shared_task
import time
import datetime
from .models import PostCategory, Post, Category
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

@shared_task #(bind=True)
def message_monday():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in_comment__gte=last_week)  # last_week
    categories = set(posts.values_list('categories__category', flat=True))  # ('categories__post', flat=True))
    subscribers = set(Category.objects.filter(category__in=categories)) #.values_list('subscribers'))#'subscribers__username', flat=True))
    print(categories, subscribers)
    # html_content = render_to_string(
    #     'daily_post.html',
    #     {
    #         'link': 'http://127.0.0.1:8000',
    #         'posts': posts,
    #     }
    # )
    # # print(subscribers)
    # msg = EmailMultiAlternatives(
    #     subject='Статьи за неделю',
    #     body='',
    #     from_email='djtest26@mail.ru',
    #     to=['psakltv@gmail.com', 'trstdjango26@gmail.com', 'rioven26rus@gmail.com', 'djtest26@yandex.ru', 'pikni4ok@gmail.com']  #subscribers,
    # )
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()

@shared_task
def send_create_message(pk):
    post = Post.objects.get(pk=pk)
    categories = post.categories.all()
    title = post.title
    subscribers = []
    for category in categories:
        subscribers_user = category.subscribers.all()
        for sub_user in subscribers_user:
            subscribers.append(sub_user.email)
    html_content = render_to_string(
        'message.html',
        {
            'link': f'http://127.0.0.1:8000/{pk}',
            'posts': post.preview,
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email='djtest26@mail.ru',
        to=subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


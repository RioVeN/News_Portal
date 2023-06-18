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

@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)

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


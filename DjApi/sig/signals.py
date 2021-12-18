import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Blog


@receiver(post_save, sender=Blog)
def say_create_post(sender, **kwargs):
    data=requests.get('https://jsonplaceholder.typicode.com/users/1')
    data=data.json()
    print('Создался Блог')
    print(data)
    print(kwargs)

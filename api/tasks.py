import string
from .models import Student
from django.utils.crypto import get_random_string
import random
from celery import shared_task

@shared_task
def create_std(totl=20):
    for i in range(totl):
        name = f'user_{get_random_string(10, string.ascii_letters)}'
        email = f'{name}@gmail.com'
        contact = random.randint(1111111111, 9999999999)
        address = f'address_{get_random_string(10, string.ascii_letters)}'

        Student.objects.create(name=name, email=email, contact=contact, address=address)
    return f'{totl} random students are created'
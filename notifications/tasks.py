from __future__ import absolute_import, unicode_literals
from celery import shared_task


@shared_task
def sum(a,b):
    return a+b

@shared_task
def send_mail(email):
    print(f"a sample mail send to {email}")
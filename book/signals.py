from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def book_handler(sender, **kwargs):
    print("Книга создалась!")
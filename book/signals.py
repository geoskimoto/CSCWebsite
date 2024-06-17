from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.utils import timezone
from .models import Member

@receiver(user_logged_in, sender=Member)
def update_last_login(sender, user, request, **kwargs):
    user.last_login = timezone.now()
    user.save()

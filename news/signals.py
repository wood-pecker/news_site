from django.dispatch import receiver
from django.db.models.signals import post_save

from news.tasks import send_new_post_notification

from .models import News

@receiver(post_save, sender=News)
def created_news(
    sender, instance: News, raw, using, update_fields, created, **kwargs
):
    if created and instance.is_published:
        send_new_post_notification.delay(instance.id, instance.title, instance.category)
    
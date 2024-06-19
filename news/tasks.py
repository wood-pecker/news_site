import smtplib
from django.core.mail import send_mail

from mysite import settings
from news.models import News
from mysite.celery import app

# @app.task
# def send_email_task(subject, message, sender, recipients, html_message=None):
#     try:
#         send_mail(
#             subject, message, sender, recipients, html_message=html_message
#         )
#     except smtplib.SMTPException:
#         invalid_users = User.objects.filter(
#             email__in=recipients,
#             is_active=False
#         )
#         for invalid_user in invalid_users:
#             if invalid_user.photo:
#                 invalid_user.photo.delete()
#             invalid_user.delete()


@app.task
def send_new_post_notification(news_id, news_title, category_id):
    # Выбрать из БД всех пользователей с подпиской, у которых включена рассылка.
    # Разослать уведомления. Первая строка - title, вторая - ссылка на статью
    # Получить все подписки на д
    send_mail(
        # news.title, 
        # news.content,
        news_id,
        news_title,
        settings.EMAIL_HOST_USER,
        ["wspanialyogorek@mail.ru"],
        fail_silently=True,
    )
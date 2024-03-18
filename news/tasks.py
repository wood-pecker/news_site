import smtplib
from django.core.mail import send_mail

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
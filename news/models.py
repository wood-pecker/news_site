from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

        
class Category(models.Model):
    title = models.CharField(
        max_length=150, db_index=True, verbose_name='Наименование категории'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news", kwargs={"pk": self.pk})
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    phone = models.CharField(max_length=20, blank=True)
    telegram = models.CharField(blank=True)
    # allow_phone_notification = models.BooleanField()
    allow_email_notifications = models.BooleanField(blank=True, default=True)
    allow_telegram_notifications = models.BooleanField(blank=True, default=False)
    is_phone_verified = models.BooleanField(null=True, blank=True, default=None)
    is_telegram_verified = models.BooleanField(null=True,   blank=True, default=None)
    phone_verification_code = models.CharField(max_length=4, blank=True)
    telegram_verification_code = models.CharField(max_length=4, blank=True)
    categories = models.ManyToManyField(Category, related_name='users')
    
    class Meta:
        verbose_name = 'Настройки пользователя'
        verbose_name_plural = 'Настройки пользователей'
        
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
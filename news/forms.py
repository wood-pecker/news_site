import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

from news.models import *


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "is_published", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={"class": "form-control" ,"rows": 5}
            ),
            "category": forms.Select(attrs={"class": "form-control"})
        }
        
    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r"\d", title):
            raise ValidationError("Название не должно начинаться с цифры!")
        return title


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = [
            'phone', 'telegram', 'allow_email_notifications', 
            'allow_telegram_notifications'
        ]
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SubscriptionForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = UserSettings
        fields = ['categories']        


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Пароль", 
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class ContactForm(forms.Form):
    subject = forms.CharField(
        label="Тема", 
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    content = forms.CharField(
        label="Текст", 
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
    )
    captcha = CaptchaField()


class UserRegisterForm(UserCreationForm):
    username = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        label="Пароль", 
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Подтверждение пароля", 
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        label="Имя", 
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        label="Фамилия", 
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    
    class Meta:
        model = User
        fields = (
            "username", "first_name", "last_name", "password1", "password1"
        )

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite import settings
from .models import Category, News
from .forms import *


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'title': 'Список новостей',
        'news': news
    }
    return render(request, template_name='news/index.html', context=context)


def test(request):
    # send_mail() 
    return HttpResponse('Test page')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'], 
                form.cleaned_data['content'],
                settings.EMAIL_HOST_USER,
                ["wspanialyogorek@mail.ru"],
                fail_silently=True,
            )
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки!')
    else:
        form = ContactForm()
    return render(request, 'news/contact.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.instance.email = form.instance.username
            user = form.save()
            login(request, user)
            messages.info(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

    
def get_category(request, category_id):
    news = News.objects.filter(category=category_id)
    current_category = Category.objects.filter(pk=category_id).first()
    context = {
        'news': news, 
        'title': 'Список новостей',
        'current_category': current_category,
    }
    return render(request, 'news/category.html', context)


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')
    
    
class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    allow_empty = False
    context_object_name = 'news'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_category = Category.objects.get(pk=self.kwargs['category_id'])
        context['title'] = current_category
        context['current_category'] = current_category
        return context

    def get_queryset(self):
        return News.objects.filter(
            is_published=True, category_id=self.kwargs['category_id'],
        ).select_related('category')
        
        
class ViewNews(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'news/view_news.html'
    
    
class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    raise_exception = True
    

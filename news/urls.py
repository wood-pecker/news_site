from django.urls import path
from django.conf.urls.static import static

from mysite import settings
from .views import *


urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('test/', test),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('contact/', contact, name='contact'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django import template
from django.db.models import Count, Sum, F

from news.models import Category

register = template.Library()


@register.inclusion_tag("news/list_categories.html")
def show_categories(current_category):
    categories = Category.objects.annotate(
        amount_news=Count("news", filter=F("news__is_published"))
    ).filter(amount_news__gt=0).order_by("title")
    return {"categories": categories, "current_category": current_category}

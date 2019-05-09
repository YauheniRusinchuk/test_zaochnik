from django.shortcuts import render
from django.db.models import (
    Count,
)


def index(request):
    cat_not_pub = Category.objects.filter(publication=False)
    articles = Article.objects.annotate(
        num_cat=Count('categories')
    ).filter(
        num_cat__lte=3, publication=True,
    ).exclude(categories__in=cat_not_pub).order_by('-created')
    return render(request, 'base.html', {'articles': articles})

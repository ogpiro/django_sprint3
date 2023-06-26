from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Category, Post

AMOUNT_NEWS = 5  # Колличество новостей (const)


def get_posts():
    return Post.objects.filter(pub_date__lte=timezone.now(),
                               is_published=True,
                               category__is_published=True)


def index(request):
    post_list = get_posts().order_by('-pub_date')[:AMOUNT_NEWS]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    post = get_object_or_404(get_posts(), id=id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    post_list = category.posts.filter(pub_date__lte=timezone.now(),
                                      is_published=True)
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)

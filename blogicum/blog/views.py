from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Category, Post


def index(request):
    current_time = timezone.now()
    post_list = Post.objects.filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    current_time = timezone.now()
    post = get_object_or_404(
        Post,
        id=id,
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
        )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    current_time = timezone.now()
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
        )
    post_list = Post.objects.filter(
        category=category,
        pub_date__lte=current_time,
        is_published=True
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)

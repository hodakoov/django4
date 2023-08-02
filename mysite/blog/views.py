from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list,3) # пагинация по 3 поста на страницу. Передаем посты и сколько постов
    page_number = request.GET.get('page',default=1) # извлекаем параметр номера страницы, если нет по умолчанию 1
    posts = paginator.page(page_number)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

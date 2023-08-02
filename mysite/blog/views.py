from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


class PostListView(ListView):
    """
    Альтернативное представление списка постов на основе класса
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)  # пагинация по 3 поста на страницу. Передаем посты и сколько постов
    page_number = request.GET.get('page', default=1)  # извлекаем параметр номера страницы, если нет по умолчанию 1
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:  # Если page_number не целое число, то выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:  # Если page_number находится вне диапазона, то выдать последнюю страницу
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

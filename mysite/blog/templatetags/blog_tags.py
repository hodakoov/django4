from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

from ..models import Post

register = template.Library()


# Создание шаблонного фильтра для поддержки синтаксиса Markdown
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


# Получаем общее число опубликованных в блоге постов
@register.simple_tag  # обрабатывает предоставленные данные и возвращает строковый литерал
def total_posts():
    return Post.published.count()


# Отображать последние посты на боковой панели блога
@register.inclusion_tag('blog/post/latest_posts.html')  # -//- и возвращает прорисованный шаблон
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# Отображать посты с наибольшим числом комментариев.
@register.simple_tag  # простой шаблонный тег, который возвращает значение(я)
def get_most_commented_posts(count=5):
    # агрегируется общее число комментариев к каждому посту
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

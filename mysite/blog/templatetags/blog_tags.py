from django import template
from ..models import Post

register = template.Library()


# Получаем общее число опубликованных в блоге постов
@register.simple_tag  # обрабатывает предоставленные данные и возвращает строковый литерал
def total_posts():
    return Post.published.count()


# Отображать последние посты на боковой панели блога
@register.inclusion_tag('blog/post/latest_posts.html')  # -//- и возвращает прорисованный шаблон
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

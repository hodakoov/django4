from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):  # определили конкретно-прикладную карту сайта
    changefreq = 'weekly'  # частотa изменения страниц постов
    priority = 0.9  # релевантность постов на веб-сайте (максимальное значение равно 1).

    def items(self):  # возвращает набор запросов QuerySet объектов, подлежащих включению в эту карту сайта
        return Post.published.all()

    def lastmod(self, obj):  # получает каждый возвращаемый методом items() объект и возвращает время последнего изменения объекта
        return obj.updated

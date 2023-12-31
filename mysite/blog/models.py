from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    '''
    Собственный менеджер для ORM место objects или конкретно-прикладной менеджер.
    Наш менеджер фильтрует посты по их статусу и возвращает поочередный набор запросов QuerySet,
    содержащий посты только со статусом PUBLISHED.
    '''

    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):  # перечисляемый класс Status для выбора вариантов статуса поста
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)  # автоматическое добавление даты при создании
    updated = models.DateTimeField(auto_now=True)  # обновление даты автоматически при сохранении
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)  # статус постов
    tags = TaggableManager() # Модель Tag используется для хранения тегов. Она содержит поля name и slug.


    # Первый объявленный в модели менеджер становится менеджером, который используется по умолчанию.
    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        ordering = ['-publish']  # сортировка в БД Сначала последние посты
        indexes = [models.Index(fields=['-publish'])]  # позволяет определять в модели индексы базы данных

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # возвращает текстовый Url, а не id как обычно
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created']),]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

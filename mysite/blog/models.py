from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    class Status(models.TextChoices): # перечисляемый класс Status для выбора вариантов статуса поста
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) # автоматическое добавление даты при создании
    updated = models.DateTimeField(auto_now=True) # обновление даты автоматически при сохранении
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT) # статус постов

    class Meta:
        ordering = ['-publish'] # сортировка в БД Сначала последние посты
        indexes = [models.Index(fields=['-publish'])] # позволяет определять в модели индексы базы данных

    def __str__(self):
        return self.title

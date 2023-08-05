from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Отображение снаружи
    list_display = ['title', 'slug', 'author', 'publish', 'status']  # отображение в странице списка постов
    list_editable = ['author', 'status'] # редактирование на странице списка изменений.

    # Отображение внутри
    radio_fields = {
        "status": admin.HORIZONTAL}  # отображение становиться в виде radiо (точки выбора). Можно вертикально
    # raw_id_fields = ['author'] # поле author отображается поисковым виджетом, а не выпадающим списком

    # Автоматическое создание slug в соответствии с названием title
    prepopulated_fields = {'slug': ('title',)}

    # Фильтрация и поиск и навигация
    list_filter = ['status', 'created', 'publish', 'author']  # боковая панель с фильтрацией
    search_fields = ['title', 'body']  # Список поле по которым можно выполнять поиск в строке поиска
    date_hierarchy = 'publish'  # ниже строки поиска отображаются навигационные ссылки для навигации по датам

    # Сортировка
    ordering = ['status', 'publish']  # сортировка на странице списка постов


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']

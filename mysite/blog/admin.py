from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # отображение в странице списка постов
    list_filter = ['status', 'created', 'publish', 'author'] # боковая панель с фильтрацией
    search_fields = ['title', 'body'] # Список поле по которым можно выполнять поиск в строке поиска
    prepopulated_fields = {'slug': ('title',)} # теперь slug добавляется автоматически копируя текст с title
    raw_id_fields = ['author'] # поле author отображается поисковым виджетом, а не выпадающим списком
    date_hierarchy = 'publish' # ниже строки поиска отображаются навигационные ссылки для навигации по датам
    ordering = ['status', 'publish'] # сортировка на странице списка постов


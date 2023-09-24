from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from .models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'short_text_field', 'pub_date', 'author',  'get_photo')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

    def get_photo(self, object):
        if object.image and hasattr(object.image, 'url'):
            return mark_safe(f'<img src="{object.image.url}" width=50>')
        else:
            return "Нет изображения"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)
    search_fields = ('name',)
    list_filter = ('color',)
    empty_value_display = '-пусто-'

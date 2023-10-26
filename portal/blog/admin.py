from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from martor.widgets import AdminMartorWidget

from blog.models import Post, Tag, PostTag

class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    list_display = ('title', 'short_text_field', 'pub_date', 'author',
                    'get_photo', 'show_tags')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    inlines = (PostTagInline,)

    def get_photo(self, object):
        if object.image and hasattr(object.image, 'url'):
            return mark_safe(f'<img src="{object.image.url}" width=50>')
        else:
            return "Нет изображения"

    def show_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    show_tags.short_description = 'Tags'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)
    search_fields = ('name',)
    list_filter = ('color',)
    empty_value_display = '-пусто-'

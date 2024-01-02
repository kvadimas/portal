from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from django.utils.safestring import mark_safe

from blog.models import Post, Tag, PostTag, TechPost, Images


class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1


class ImagesInline(admin.StackedInline):
    model = Images
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    list_display = ('title', 'short_text_field', 'pub_date', 'author',
                    'show_tags', 'posting', 'get_label')
    readonly_fields = ('get_images',)
    search_fields = ('text',)
    list_filter = ('pub_date','posting')
    empty_value_display = '-пусто-'
    inlines = (PostTagInline, ImagesInline)
    prepopulated_fields = {"url": ("title",)}

    def get_label(self, object):
        if object.label and hasattr(object.label, 'url'):
            return mark_safe(f'<img src="{object.label.url}" width=50>')
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


@admin.register(TechPost)
class TechPostAdmin(admin.ModelAdmin):
    readonly_fields = ('get_images',)
    inlines = (ImagesInline,)
    prepopulated_fields = {"url": ("title",)}


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('get_photo', 'alt', 'get_jpg_png', 'get_webp', 'title',)
    readonly_fields = ('get_photo',)

    def get_jpg_png(self, object):
        if object.jpg_png:
            return True
        return False

    def get_webp(self, object):
        if object.webp:
            return True
        return False

from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from martor.widgets import AdminMartorWidget

from blog.models import Post, Tag, PostTag, TechPost, Images

class BaseBlogAdmin(admin.ModelAdmin):
    ''' Для некоторых функций'''
    get_photo = None

    def get_photo(self, object):
        if object.jpg_png and hasattr(object.jpg_png, 'url'):
            return mark_safe(f'<img src="{object.jpg_png.url}" width=50>')
        if object.webp and hasattr(object.webp, 'url'):
            return mark_safe(f'<img src="{object.webp.url}" width=50>')
        else:
            return "Нет изображения"

class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(Post)
class PostAdmin(BaseBlogAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    list_display = ('title', 'short_text_field', 'pub_date', 'author',
                    'show_tags', 'posting') #  'get_photo'
    search_fields = ('text',)
    list_filter = ('pub_date','posting')
    empty_value_display = '-пусто-'
    inlines = (PostTagInline, ImagesInline)
    prepopulated_fields = {"url": ("title",)}

#    def get_photo(self, object):
#        if object.image and hasattr(object.image, 'url'):
#            return mark_safe(f'<img src="{object.image.url}" width=50>')
#        else:
#            return "Нет изображения"

    def show_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    show_tags.short_description = 'Tags'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)
    search_fields = ('name',)
    list_filter = ('color',)
    empty_value_display = '-пусто-'


#  @admin.register(TechPost)
#  class TechPostAdmin(BaseBlogAdmin):


@admin.register(Images)
class ImagesAdmin(BaseBlogAdmin):
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

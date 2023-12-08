from django.contrib.auth import get_user_model
from django.core import validators
from django.template.defaultfilters import truncatechars
from django.db import models

from martor.models import MartorField

User = get_user_model()


class Tag(models.Model):
    name = models.CharField('Название', max_length=250)
    color = models.CharField('Цвет в HEX', max_length=7, unique=True)
    slug = models.SlugField('Уникальный слаг', max_length=200, unique=True)
    posts = models.ManyToManyField("Post", through='PostTag')

    def __str__(self):
        return f'{self.name} - {self.slug}'

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['name']


class Post(models.Model):
    pub_date = models.DateTimeField('Дата', auto_now_add=True)
    url = models.SlugField('Url', max_length=100)
    tags = models.ManyToManyField(Tag, through='PostTag')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=250)
    image = models.ImageField(
        'Ссылка на картинку на сайте',
        upload_to='blog/images/',
        blank=True,
        null=True,
    )
    text = MartorField('Текст')
    description = MartorField(
        'Описание',
        blank=True,
        null=True,
        max_length=600
    )
    posting = models.BooleanField("Публикация на сайте", default=False)

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = self.text[:600]
        super(Post, self).save(*args, **kwargs)

    def short_text_field(self):
        return truncatechars(self.text, 50)

    short_text_field.short_description = 'Описание'

    def __str__(self):
        return f'{self.author} - {self.pub_date} - {self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} добавил {self.post} в избранное'

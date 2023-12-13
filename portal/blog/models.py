from django.contrib.auth import get_user_model
from django.template.defaultfilters import truncatechars
from django.db import models
from django.utils.safestring import mark_safe

from martor.models import MartorField

User = get_user_model()


class Tag(models.Model):
    name = models.CharField('Название', max_length=250)
    color = models.CharField('Цвет в HEX', max_length=7, unique=True)
    slug = models.SlugField('Уникальный слаг', max_length=200, unique=True)
    posts = models.ManyToManyField("Post", through='PostTag')

    def __str__(self) -> str:
        return f'{self.name} - {self.slug}'

    class Meta:
        verbose_name: str = 'Тег'
        verbose_name_plural: str = 'Теги'
        ordering = ['name']


class Post(models.Model):
    pub_date = models.DateTimeField('Дата', auto_now_add=True)
    url = models.SlugField('Url', max_length=100)
    tags = models.ManyToManyField(Tag, through='PostTag')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=250)
    #  Меняю способ хранения картинок
    #  image = models.ImageField(
    #      'Ссылка на заглавную картинку на сайте',
    #      upload_to='blog/images/',
    #      blank=True,
    #      null=True,
    #  )
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

    def get_images(self):
        image = Images.objects.filter(post=self)
        st: str = ''
        if image:
            for i in image:
                st += f'<img src="/media/{i.jpg_png}" width=50>'
            return mark_safe(st)
        return "Нет изображения"

    short_text_field.short_description: str = 'Описание'
    get_images.short_description: str = "Миниатюры"

    def __str__(self) -> str:
        return f'{self.author} - {self.pub_date} - {self.title}'

    class Meta:
        verbose_name: str = 'Пост'
        verbose_name_plural: str = 'Посты'


class PostTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} добавил {self.post} в избранное'

class Images(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    jpg_png = models.ImageField(
        'Ссылка на картинку jpg/png',
        upload_to='blog/images/',
        blank=True,
        null=True,
    )
    webp = models.ImageField(
        'Ссылка на картинку webp',
        upload_to='blog/images/',
        blank=True,
        null=True,
    )
    alt = models.CharField(
        'Текстовое описание изображения',
        max_length=50,
        blank=True,
        null=True
    )
    title = models.CharField(
        'Всплывающая подсказка при наведении курсора',
        max_length=50,
        blank=True,
        null=True
    )

    def get_photo(self):
        if self.jpg_png and hasattr(self.jpg_png, 'url'):
            return mark_safe(f'<img src="{self.jpg_png.url}" width=50>')
        if self.webp and hasattr(self.webp, 'url'):
            return mark_safe(f'<img src="{self.webp.url}" width=50>')
        else:
            return "Нет изображения"

    get_photo.short_description: str = "Миниатюра"

    def __str__(self) -> str:
        return f'{self.alt} - {self.jpg_png}'

    class Meta:
        verbose_name: str = 'Картинка'
        verbose_name_plural: str = 'Картинки'


class TechPost(Post):
    '''Пост для постоянных статей, таких как about'''
    pass

    class Meta:
        verbose_name: str = 'Стабильная статья'
        verbose_name_plural: str = 'Стабильные статьи'

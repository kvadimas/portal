from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

USER_ROLES = (
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
)


class User(AbstractUser):
    """
    Кастомная модель User. Необходима, тк нужно добавить
    несколько нестандартных полей.
    """
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': 'Такой username уже занят.',
        },
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=254,
        blank=False,
        unique=True,
        null=False,
        error_messages={
            'unique': 'Такой email уже зарегистрирован.',
        },
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True,
    )
    karma = models.IntegerField(
        verbose_name='Карма',
        default=0,
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=15,
        choices=USER_ROLES,
        default='user',
    )

    profile_pic = models.ImageField(
        'Аватарка',
        upload_to='blog/images/',
        blank=True,
        null=True,
    )

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_query_name='custom_user',
        related_name='custom_user_set', # изменён related_name
        help_text='Группы, к которым принадлежит этот пользователь.'
                   'Пользователь получит все разрешения предоставленные'
                   'каждой из их групп.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_query_name='custom_user',
        related_name='custom_user_permission_set', # изменён related_name
        help_text='Особые разрешения для этого пользователя.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f'{self.username}'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin'

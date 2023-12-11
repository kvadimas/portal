# Generated by Django 4.2.6 on 2023-12-11 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_image_alter_post_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "jpg_png",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/images/",
                        verbose_name="Ссылка на картинку jpg/png",
                    ),
                ),
                (
                    "webp",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/images/",
                        verbose_name="Ссылка на картинку webp",
                    ),
                ),
                (
                    "alt",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Текстовое описание изображения",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Всплывающая подсказка при наведении курсора",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TechPost",
            fields=[
                (
                    "post_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="blog.post",
                    ),
                ),
            ],
            bases=("blog.post",),
        ),
        migrations.DeleteModel(
            name="Image",
        ),
    ]
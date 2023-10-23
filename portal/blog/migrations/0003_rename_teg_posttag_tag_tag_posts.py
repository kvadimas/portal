# Generated by Django 4.2.5 on 2023-10-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_description_alter_post_text"),
    ]

    operations = [
        migrations.RenameField(
            model_name="posttag",
            old_name="teg",
            new_name="tag",
        ),
        migrations.AddField(
            model_name="tag",
            name="posts",
            field=models.ManyToManyField(through="blog.PostTag", to="blog.post"),
        ),
    ]

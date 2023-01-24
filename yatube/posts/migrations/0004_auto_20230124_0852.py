# Generated by Django 2.2.16 on 2023-01-24 05:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_auto_20221216_2032"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-pub_date"]},
        ),
        migrations.AlterField(
            model_name="group",
            name="description",
            field=models.TextField(
                help_text="Введите описание группы", verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="slug",
            field=models.SlugField(
                help_text="Укажите ссылку на группу",
                unique=True,
                verbose_name="Ссылка на группу",
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="title",
            field=models.CharField(
                help_text="Введите название группы",
                max_length=200,
                verbose_name="Название",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор публикации",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="group",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите группу",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="posts.Group",
                verbose_name="Группа",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Дата публикации"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.TextField(
                help_text="Введите текст поста", verbose_name="Текст записи"
            ),
        ),
    ]

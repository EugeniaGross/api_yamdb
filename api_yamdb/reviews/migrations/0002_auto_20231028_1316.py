# Generated by Django 3.2 on 2023-10-28 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.RemoveField(
            model_name='comments',
            name='title',
        ),
    ]

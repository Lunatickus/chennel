# Generated by Django 4.1.5 on 2023-02-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_mini_text_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mini_text',
            field=models.TextField(max_length=5000, verbose_name='Краткое содержание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=10000000, verbose_name='Полное содержание'),
        ),
    ]

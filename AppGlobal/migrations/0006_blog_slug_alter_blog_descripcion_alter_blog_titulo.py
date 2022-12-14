# Generated by Django 4.1.1 on 2022-10-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGlobal', '0005_alter_blog_descripcion_alter_blog_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='blogs', max_length=90, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='descripcion',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]

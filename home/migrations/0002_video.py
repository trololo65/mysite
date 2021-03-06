# Generated by Django 3.2.8 on 2021-10-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('date_start', models.CharField(max_length=50, verbose_name='Дата выхода')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('poster', models.ImageField(upload_to='image/poster')),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]

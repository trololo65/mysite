# Generated by Django 3.2.8 on 2021-10-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='full_text',
            field=models.TextField(default=134, verbose_name='О фильме'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='zjanr',
            field=models.CharField(default=324, max_length=50, verbose_name='Жанр'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=80, verbose_name='Название'),
        ),
    ]
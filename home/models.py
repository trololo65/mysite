from django.db import models


class History(models.Model):
    title = models.CharField("Название", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField("История")
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/history/{self.id}'

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = "Истории"


class Music(models.Model):
    title = models.CharField("Название", max_length=50)
    music_len = models.CharField("Анонс", max_length=10)
    date = models.DateTimeField("Дата публикации")
    url = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/music/{self.id}'

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = "Музыка"


class Other(models.Model):
    title = models.CharField("Название", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField("История")
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/other/{self.id}'

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = "Статьи"

class Video(models.Model):
    title = models.CharField("Название", max_length=80)
    anons = models.CharField("Анонс", max_length=250)
    zjanr = models.CharField("Жанр", max_length=50)
    full_text = models.TextField("О фильме")
    date_start = models.CharField("Дата выхода", max_length=50)
    date = models.DateTimeField("Дата публикации")
    poster = models.ImageField(upload_to='image/poster')
    url = models.URLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/video/{self.id}'

    class Meta:
        verbose_name = 'Пост видео'
        verbose_name_plural = "Посты видео"

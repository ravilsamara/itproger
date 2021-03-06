from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новость'

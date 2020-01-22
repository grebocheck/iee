import datetime
from django.db import models

from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Название статьи' , max_length = 200)
    article_text = models.TextField('Текст статьи')
    pub_data = models.DateTimeField('Дата публикации')
    article_image = models.ImageField(height_field=None, width_field=None,null = True , blank = True , upload_to = "images/" , verbose_name = 'Изображение')
    author = models.CharField('Автор', max_length = 50 , default = 'Admin')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_data >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = 'Статті'

class Coment(models.Model):
    article = models.ForeignKey(Article , on_delete = models.CASCADE)
    author_name = models.CharField('Имя коментатора',  max_length = 50)
    coment_text = models.CharField('Текст коментария', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Коментарій"
        verbose_name_plural = 'Коментарі'


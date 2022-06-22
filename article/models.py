from django.db import models
from users.models import CustomUser


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок статьи', max_length=150)
    text = models.TextField(verbose_name='Текст статьи')
    author = models.ForeignKey(CustomUser,  verbose_name='Автор статьи', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации статьи')
    public = models.BooleanField(default=False, verbose_name='Публичная статья')

    def __str__(self):
        return self.title

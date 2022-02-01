from django.db import models
from django.urls import reverse, reverse_lazy


class Post(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(verbose_name='Картинка', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("index")


class Comment(models.Model):
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse_lazy("index")


class Message(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.title

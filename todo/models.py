from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название задачи')
    is_completed = models.BooleanField(default=False, verbose_name='Готовность')
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             verbose_name='Задача пользователя', null=True, blank=True, related_name='tasks')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:update', kwargs={'id_task': self.pk})

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'

    objects = models.Manager()
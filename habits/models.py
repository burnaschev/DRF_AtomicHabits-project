from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasurable = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    associated_habit = models.ForeignKey(
        'self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    period = models.IntegerField(default=1, verbose_name='период выполнения, в днях')
    reward = models.CharField(max_length=250, verbose_name='награда')
    duration = models.IntegerField(default=0, verbose_name='время на выполнение в секундах')
    is_public = models.BooleanField(default=True, verbose_name='признак публикации')
    send_time = models.TimeField(auto_now=True, **NULLABLE, verbose_name='Время отправки')

    def __str__(self):
        return f'{self.place} ( {self.time} ): {self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

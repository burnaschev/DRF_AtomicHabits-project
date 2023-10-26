from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    tg_name = models.CharField(unique=True, max_length=32, verbose_name='имя в телеграм')
    chat_id = models.PositiveBigIntegerField(verbose_name='chat id', **NULLABLE)


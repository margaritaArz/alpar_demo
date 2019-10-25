from django.db import models


class ParsingSettings(models.Model):
    class Meta:
        verbose_name = 'Настройки для парсинга'
        verbose_name_plural = 'Настройки для парсинга'

    worker_name = models.TextField(verbose_name='Имя воркера')
    firefox_profile = models.TextField(verbose_name='Путь до профиля мозиллы')
    sleeping_time = models.IntegerField(verbose_name='Время между итерациями(в минутах)', default=3)
    start_iteration_time = models.DateTimeField(verbose_name='Дата и время начала итерации', default=None, null=True)
    finish_iteration_time = models.DateTimeField(verbose_name='Дата и время окончания итерации', default=None, null=True)
    last_ping_time = models.DateTimeField(verbose_name='Дата и время окончания итерации', default=None, null=True)

    def __str__(self):
        return self.worker_name

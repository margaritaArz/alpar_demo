from django.db import models


class ParsingTasks(models.Model):
    class Meta:
        verbose_name = 'Задача для парсинга'
        verbose_name_plural = 'Задачи для парсинга'

    link = models.TextField(verbose_name='Ссылка')

    def __str__(self):
        return self.link

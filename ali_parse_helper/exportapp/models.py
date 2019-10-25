from django.db import models
from mainapp.models import ParsingResults, ParsingTasks


class ExportHistory(models.Model):
    class Meta:
        verbose_name = 'Таблица экспорта'
        verbose_name_plural = 'Таблица экспорта'

    results_id = models.ManyToManyField(ParsingResults, verbose_name='ID результатов', related_name='results_ids')
    out_file_path = models.TextField(verbose_name='Путь выгрузки отчёта', default=None, null=True)
    catch_time = models.DateTimeField(verbose_name='Дата и время построения отчёта', default=None, null=True)

    def __str__(self):
        return f'{self.pk}|{self.out_file_path}'

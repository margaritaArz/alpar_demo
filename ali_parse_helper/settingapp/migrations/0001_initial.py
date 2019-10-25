# Generated by Django 2.2.5 on 2019-10-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParsingSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.TextField(verbose_name='Имя воркера')),
                ('firefox_profile', models.TextField(verbose_name='Путь до профиля мозиллы')),
                ('sleeping_time', models.IntegerField(default=3, verbose_name='Время между итерациями(в минутах)')),
                ('start_iteration_time', models.DateTimeField(default=None, null=True, verbose_name='Дата и время начала итерации')),
                ('finish_iteration_time', models.DateTimeField(default=None, null=True, verbose_name='Дата и время окончания итерации')),
                ('last_ping_time', models.DateTimeField(default=None, null=True, verbose_name='Дата и время окончания итерации')),
            ],
            options={
                'verbose_name': 'Настройки для парсинга',
                'verbose_name_plural': 'Настройки для парсинга',
            },
        ),
    ]
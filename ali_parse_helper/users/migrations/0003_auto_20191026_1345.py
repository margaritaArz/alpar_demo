# Generated by Django 2.2.5 on 2019-10-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191023_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
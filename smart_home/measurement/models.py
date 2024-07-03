from django.db import models


# Create your models here.
class Measurement(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')


class Sensor(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    update_date_time = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

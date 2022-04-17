from django.db import models

class Sensor(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.CharField(max_length=400, verbose_name="Описание")


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurement")
    temperature = models.FloatField(verbose_name="Температура")
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)



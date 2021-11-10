from django.db import models


class Auto(models.Model):
    name = models.CharField(max_length=50, verbose_name='Марка авто')
    price = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена авто', null=True, blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name='Модель авто')
    details = models.ManyToManyField('Detail', verbose_name='Запчасти авто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Brand(models.Model):
    name = models.CharField(max_length=250, verbose_name='Брэнд авто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Detail(models.Model):
    name = models.CharField(max_length=250, verbose_name='Детали авто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'

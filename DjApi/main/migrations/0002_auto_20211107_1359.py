# Generated by Django 3.2.8 on 2021-11-07 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auto',
            options={'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='detail',
            options={'verbose_name': 'Деталь', 'verbose_name_plural': 'Детали'},
        ),
    ]

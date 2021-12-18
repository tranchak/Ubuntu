from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100,verbose_name='Обложка')
    author=models.ForeignKey('Author', on_delete=models.CASCADE,verbose_name='Автор')
    discription=models.TextField(verbose_name='Описание')


class Author(models.Model):
    name=models.CharField(max_length=1000, verbose_name='Имя')


    def __str__(self):
        return self.name




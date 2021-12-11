from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    owner = models.ForeignKey('Owner',on_delete=models.CASCADE, null=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    pubdate = models.DateField()

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Owner(models.Model):
    name=models.CharField(max_length=130)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=100, blank=True, null=True)
    model=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)



    def __str__(self):
        return self.model





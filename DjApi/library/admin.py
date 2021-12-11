from django.contrib import admin

# Register your models here.
from .models import Author, Publisher, Book, Store, Car, Owner

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)
admin.site.register(Owner)
admin.site.register(Car)
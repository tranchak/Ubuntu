from django.shortcuts import render

# Create your views here.
from .models import Book, Author, Store, Publisher


def get_main(request):
    # books = Book.objects.all()
    # authors = Author.objects.all()
    # stores = Store.objects.all()
    # book = Book.objects.get(pk=1)
    # print(book.publisher, 'get')
    # book1=Book.objects.select_related('publisher').get(pk=1)
    # print(book1.publisher, 'select')
    # print(book1.owner,'owner')
    # book2=Publisher.objects.select_related().get(pk=1)
    store=Store.objects.prefetch_related('books')
    store_select=Book.objects.select_related('publisher').filter(publisher__name='Новый двор')
    print('15 строка',store)
    print('18 строка',store_select)

    contex = {}
    return render(request, 'library/library.html', contex)

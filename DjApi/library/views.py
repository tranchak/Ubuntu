from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# from django.views import View
from django.views import View
from django.views.generic import ListView, FormView

from .forms import CarForm
from .models import Book, Author, Store, Publisher


# # def get_main(request):
#     # books = Book.objects.all()
#     # authors = Author.objects.all()
#     # stores = Store.objects.all()
#     # book = Book.objects.get(pk=1)
#     # print(book.publisher, 'get')
#     # book1=Book.objects.select_related('publisher').get(pk=1)
#     # print(book1.publisher, 'select')
#     # print(book1.owner,'owner')
#     # book2=Publisher.objects.select_related().get(pk=1)
#
#     # q=Q(name__startswith='Ne')
#     # q1 = Q(name__startswith='Пи')
#     #
#     # cu = Book.objects.filter(q, q1)
#     # print(cu)
#
#     # a = Book.objects.annotate(priceF=F('price')*1000)
#     # print(a[0].priceF)
#
#     # b = Book.objects.get(name='New')
#     # b.price = int(b.price)+1
#     # b.save()
#     # print(b)
#     # a = Author.objects.value(F('name') + (F('age')))
#     # print(a)
#
#     # a = Book.objects.values('price')
#     # b = Auto.objects.values('price')
#     a = Book.objects.values('name')
#     b = Store.objects.values('name')
#     # c = a.intersection(b) # введит queryset похожего элемента (двух или более)
#     # c = a.difference(b)  # введит queryset только одного запроса и уберет дубликаты
#     c = a.union(b)  # введит queryset без повторяющихся элементов (дубликатов не будет)
#     print(c)
#
#
#     store=Store.objects.prefetch_related('books')
#     store_select=Book.objects.select_related('publisher').filter(publisher__name='Новый двор')
#     print('15 строка',store)
#     print('18 строка',store_select)
#
#     contex = {}
#     # return render(request, 'library/library.html', contex)

# class MyView(View):
#     name='Johan'
#     age=0
#     print(age)
#     def get(self, request):
#         print(self.name,self.age)
#         # return HttpResponse('Hello')
#         return render(request,'library/api.html',{'name':self.name,'age':self.age})

# class MyView(TemplateView):
#     template_name = 'library/api.html'

class MyView(ListView):
    model = Book
    template_name = 'library/api.html'

class NewView(View):
    def get(self, request):
        return render(request,template_name='library/new.html')
    def post(self,request):
        return HttpResponse('Привет метод POST')
    def put(self,request):
        return HttpResponse('Hello, I am PUT')

class MyNewView(FormView):
    form_class = CarForm
    template_name = 'library/index.html'
    success_url = '/admin/'



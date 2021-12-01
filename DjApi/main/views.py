from django.db.models import Count, F, Sum, Avg
from django.shortcuts import render
from .models import Auto, Brand, Detail


def home_page(request):
    a=Auto.objects.aggregate()
    for i in a:
        print(i.name,i.price)

    # a = Auto.objects.annotate(out=Sum('price')).aggregate(b=Avg('Out'))
    # print(dir(a))

    # etails__name'))
    # c = Auto.objectsb=Auto.objects.aggregate(out=Avg('price'))
    #     # for i in b:
    #     #     print(i.out)
    #     #     for n in a:
    #     #     # print(f'Имя авто:{i.name},цена:{i.price}, средня:{i.out}')
    #     #         print(f'Имя авто: {n.name}, цена авто:{n.price}')
    #     # # a=Auto.objects.all().annotate(out=Count('d.all().annotate(d=Count('details__name'))
    # for i in a:
    #     print(f'Имя автомобиля:{i.name}, сумма:{i.price}')
    # for i in b:
    #     print(f'Имя автомобиля:{i.name}, цена:{i.price}, сумма:{i.out}')
    # b = Auto.objects.all().aggregate(Avg('price'))
    # print(b)
    # # print(a[0].brand_id__count)
    # print('4',a.query)
    # # print(a.filter(pk=1))
    # auto=Auto.objects.create(name='Zaz',price=3,brand_id=1)
    # # print('1',type(a))
    # # print('2',a)
    # print('3',Auto.objects.filter(name='Zaz'))
    # print(a.db)
    # print(a.ordered)
    # print('4',type(a.filter(pk=1)))
    # p=Auto.objects.get(pk=1)
    # # auto = Auto.objects.raw('Select * From Main_Auto')
    # print('11111',p)
    # # print(auto.query)
    # # print(auto[0].name)
    # # print(auto.query)
    # # print(dir(Auto.objects))
    # # print(auto)
    context = {'auto':a}
    return render(request, 'main/library.html', context)

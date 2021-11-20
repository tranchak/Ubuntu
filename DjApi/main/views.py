from django.db.models import Count, F, Sum
from django.shortcuts import render
from .models import Auto, Brand, Detail


def home_page(request):
    a=Auto.objects.all().annotate(out=Count('details__name'))
    print(a[0].out)
    # print(a[0].brand_id__count)
    print(a.query)
    # print(a.filter(pk=1))
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
    context = {'auto': a}
    return render(request, 'main/index.html', context)

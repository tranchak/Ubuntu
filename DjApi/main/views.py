from django.shortcuts import render
from .models import Auto, Brand, Detail




def home_page(requests):
    auto = Auto.objects.filter(pk=3)
    print(auto.query)
    print(auto[0].brand)
    # print(auto.query)
    #print(dir(Auto.objects))
    # print(auto)
    context = {}
    return render(requests, 'main/index.html', context)

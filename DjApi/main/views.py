from django.shortcuts import render
from .models import Auto, Brand, Detail




def home_page(requests):
    auto = Auto.objects.filter()
    print(Auto.objects)
    # print(auto.query)
    print(dir(Auto.objects))
    # print(auto)
    context = {}
    return render(requests, 'main/index.html', context)

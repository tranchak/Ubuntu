from django.shortcuts import render

from .forms import Add_blog
from .signals import say_create_post

# Create your views here.

def sig_sig(request):
    form=Add_blog()
    if request.method=='POST':
        form=Add_blog(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request,'sig/index.html',context)

from django.urls import path
from .views import get_main

urlpatterns = [

    path('', get_main, name='get_name'),

]
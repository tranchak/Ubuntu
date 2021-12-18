
from django.urls import path
# from django.views.generic import TemplateView
from .views import MyView, NewView, MyNewView, form_user_view, get_stas, Johan

app_name='library'
urlpatterns = [

    path("api/", MyView.as_view(), name="classView"),
    path("new/", NewView.as_view(), name="new"),
    path("index/", MyNewView.as_view(), name="index"),
    path("form/", form_user_view, name='form'),
    path("get_stas/", get_stas, name='get_stas'),
    path("new_Oleg/", Johan, name='Johan')
]
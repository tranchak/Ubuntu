
from django.urls import path
# from django.views.generic import TemplateView
from .views import MyView, NewView, MyNewView, form_user_view

app_name='library'
urlpatterns = [

    # path("api/", MyView.as_view(), name="classView")
    path("api/", MyView.as_view(), name="classView"),
    path("new/", NewView.as_view(), name="new"),
    path("index/", MyNewView.as_view(), name="index"),
    path("form/", form_user_view, name='form')
]
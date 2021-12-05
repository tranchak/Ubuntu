
from django.urls import path
# from django.views.generic import TemplateView
from .views import MyView, NewView

app_name='library'
urlpatterns = [

    # path("api/", MyView.as_view(), name="classView")
    path("api/", MyView.as_view(), name="classView"),
    path("new/", NewView.as_view(), name="new")
]
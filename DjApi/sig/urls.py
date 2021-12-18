from django.urls import path

from .views import sig_sig

app_name = 'mixin_signal'
urlpatterns = [
    path('index/', sig_sig, name="sig_sig")

]

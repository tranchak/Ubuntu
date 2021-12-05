from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    '''Car form'''

    class Meta:
        model=Car
        fields="__all__"
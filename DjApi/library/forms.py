from django import forms
from django.core.exceptions import ValidationError

from .models import Car


class CarForm(forms.ModelForm):
    '''Car form'''
    def clean_price(self):
        price=int(self.cleaned_data['price'])
        price=price*1.2
        self.cleaned_data['price']=price
        return self.cleaned_data['price']

    class Meta:
        model=Car
        fields="__all__"

class GetPost(forms.Form):
    brand=forms.CharField(max_length=100)
    model=forms.CharField(max_length=100)
    price=forms.DecimalField(max_digits=8,decimal_places=2)

def user_cap(name):
    if not name.isupper():
        raise ValidationError('Имя должно быть большим')
    elif len(name)<5:
        raise ValidationError('Имя должно быть не менее 5 символов')
    else:
        return name


class FormUserView(forms.Form):
    username=forms.CharField(label='User Name',validators=[user_cap],
                             help_text='Верхний регистр и больше 5 символов')
    email=forms.EmailField(label='User email',
                           help_text='Правильно введите ваш email')
    note=forms.CharField(label='Note')

def validator_stas(value):
    if value <0 :
        raise ValidationError('Value should be a positive number')



class StasCarForm(forms.ModelForm):
    price=forms.DecimalField(validators=[validator_stas])

    class Meta:
        model=Car
        fields='__all__'

from django import forms

from .models import Blog


class Add_blog(forms.ModelForm):

    class Meta:
        model = Blog
        fields='__all__'

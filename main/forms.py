from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Назва продукту')
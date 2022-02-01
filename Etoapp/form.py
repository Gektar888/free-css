from django import forms
from .models import Cars, Order




class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car_type', 'drop', 'when']
        widgets = {
            'car_type' : forms.Select(attrs={"class": 'form-control'}),
            'drop' : forms.TextInput(attrs={"class": 'form-control'}),
            'when' : forms.DateTimeInput(attrs={"class": 'form-control'}),
          }
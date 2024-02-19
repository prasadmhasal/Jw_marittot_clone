from django import forms
from .models import Product ,  RoomProduct


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'

class RoomProduct(forms.ModelForm):
    class Meta:
        model = RoomProduct
        fields ='__all__'

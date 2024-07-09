from django import forms
from .models import Product, ProductSubCategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']

class ProductSubCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductSubCategory
        fields = ['product', 'price', 'image', 'model', 'ram']

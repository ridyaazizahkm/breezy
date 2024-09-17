from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "ukuran", "aroma", "top_notes", "middle_notes", "base_notes"]
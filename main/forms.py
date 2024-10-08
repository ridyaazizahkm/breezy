from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "ukuran", "aroma", "top_notes", "middle_notes", "base_notes"]
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_ukuran(self):
        ukuran = self.cleaned_data["ukuran"]
        return strip_tags(ukuran)
    
    def clean_aroma(self):
        aroma = self.cleaned_data["aroma"]
        return strip_tags(aroma)
    
    def clean_top_notes(self):
        top_notes = self.cleaned_data["top_notes"]
        return strip_tags(top_notes)
    
    def clean_middle_notes(self):
        middle_notes = self.cleaned_data["middle_notes"]
        return strip_tags(middle_notes)
    
    def clean_base_notes(self):
        base_notes = self.cleaned_data["base_notes"]
        return strip_tags(base_notes)
    
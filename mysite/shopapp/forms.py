from shopapp.models import Order, Product
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "delivery_address", "promocode", "user", "products"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    images = forms.ImageField(
        widget=forms.ClearableFileInput() # attrs={"multiple": True}
    )

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
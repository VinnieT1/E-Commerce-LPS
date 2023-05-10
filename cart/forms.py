from django import forms
from .models import BankBillInformation, CreditInformation, ShippingAdress

class ShippingAdressForm(forms.ModelForm):
    class Meta:
        model = ShippingAdress
        fields = ['address', 'city', 'state', 'state', 'zip_code']

class CreditInformationForm(forms.ModelForm):
    class Meta:
        model = CreditInformation
        fields = ['credit_card_number', 'expiration_date_month', 'expiration_date_year', 'cvc', 'name']
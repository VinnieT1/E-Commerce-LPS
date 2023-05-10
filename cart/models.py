import random
from django.db import models
from base.settings import LPS_CONFIG
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([orderitem.get_total for orderitem in orderitems])

        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([orderitem.quantity for orderitem in orderitems])

        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAdress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    
if LPS_CONFIG['payment_methods']['credit']:
    class CreditInformation(models.Model):
        MONTHS = [(i, i) for i in range(1, 13)]
        YEARS = [(i, i) for i in range(2023, 2124)]

        credit_card_number = models.CharField(max_length=20)
        expiration_date_month = models.IntegerField(choices=MONTHS)
        expiration_date_year = models.IntegerField(choices=YEARS)
        cvc = models.IntegerField()
        name = models.CharField(max_length=200)

if LPS_CONFIG['payment_methods']['bank_bill']:
    class BankBillInformation(models.Model):
        bar_code = models.CharField(max_length=45)

        def generate_fake_bill():
            numbers_list = []
            numbers_length = [5, 5, 6, 5, 6, 1, 11]
            separators = ['.', '.', ' ', '.', ' ', ' ']
            result = ''

            for length in numbers_length:
                numbers_list.append([str(random.randint(0, 9)) for i in range(length)])

            for idx, separator in enumerate(separators):
                for digit in numbers_list[idx]:
                    result += digit
                result += separator
                
            for digit in numbers_list[6]:
                result += digit

            return result

        def __init__(self):
            super().__init__(self)
            self.bar_code = BankBillInformation.generate_fake_bill()

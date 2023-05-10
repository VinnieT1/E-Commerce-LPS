from django.db import models
from base.settings import LPS_CONFIG

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
if LPS_CONFIG['products_enabled']['CPU']:
    class CPU(Product):
        number_of_cores = models.PositiveIntegerField()

        @property
        def product_type(self):
            return 'CPU'

if LPS_CONFIG['products_enabled']['GPU']:
    class GPU(Product):
        frequency = models.PositiveIntegerField()

        @property
        def product_type(self):
            return 'GPU'

if LPS_CONFIG['products_enabled']['PC']:
    class PC(Product):
        is_notebook = models.BooleanField()

        @property
        def product_type(self):
            return 'PC'

PRODUCT_TYPES = {}
for key in LPS_CONFIG['products_enabled']:
    if LPS_CONFIG['products_enabled'][key]:
        PRODUCT_TYPES[key] = globals()[key]
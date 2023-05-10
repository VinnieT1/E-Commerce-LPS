from django.shortcuts import render
from cart.models import Order
from users.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from base.settings import LPS_CONFIG
from products.views import PRODUCT_TYPES_STR

# Create your views here.
def home_view(request):
    context = {}
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    context['register_form'] = UserCreationForm()
    context['login_form'] = AuthenticationForm()
    context['product_types'] = PRODUCT_TYPES_STR

    context |= LPS_CONFIG
    return render(request, 'base.html', context)
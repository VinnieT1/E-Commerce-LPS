from django.shortcuts import render, redirect
from base.settings import LPS_CONFIG
from .models import Product, PRODUCT_TYPES
from cart.models import Order
from users.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

PRODUCT_TYPES_STR = [key for key in PRODUCT_TYPES]

# Create your views here.
def product_view(request, pk, product_type):
    context = {
        'product_type':product_type,
        'pk':pk,
    }
    context['product'] = PRODUCT_TYPES[product_type].objects.get(pk=pk)

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    context['register_form'] = UserCreationForm()
    context['login_form'] = AuthenticationForm()

    context |= LPS_CONFIG
    return render(request, 'product.html', context)

def products_view(request):
    print('requested!')
    context = {}
    context['products'] = []

    for key in PRODUCT_TYPES:
        context['products'] += PRODUCT_TYPES[key].objects.all()

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    context['register_form'] = UserCreationForm()
    context['login_form'] = AuthenticationForm()

    context |= LPS_CONFIG
    print('context is', context)
    return render(request, 'products.html', context)

def products_type_view(request, product_type):
    if product_type not in PRODUCT_TYPES_STR:
        return redirect('home')

    context = {}
    context['products'] = []

    print('type', product_type, 'was requested!')
    print('cpu:', PRODUCT_TYPES['CPU'].objects.all())

    context['products'] += (PRODUCT_TYPES[product_type].objects.all())
    context['product_type'] = product_type
    
    print(context['products'])

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        context['num_cart_items'] = order.get_cart_items

    context['register_form'] = UserCreationForm()
    context['login_form'] = AuthenticationForm()

    context |= LPS_CONFIG
    return render(request, 'products.html', context)
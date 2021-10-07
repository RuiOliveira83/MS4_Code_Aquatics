from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jhqc1LYd79hluF8b0OFNKNPuApz71fotPjwgb1xkHTTEI2E3pw10TxM5DnKa02uxleLm6H6MrmLgsirvf5k35Md00gWlDTQ71',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

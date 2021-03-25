from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddItemForm
from blog.models import Post

@require_POST
def cart_add(request, post_id):
    cart = Cart(request)
    post = get_object_or_404(Post, id=post_id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(post=post,
                quantity = cd['quantity'],
                update_quanity = cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, post_id):
    cart = Cart(request)
    post = get_object_or_404(Post, id=post_id)
    cart.remove(post)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quanity_form'] = CartAddItemForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})

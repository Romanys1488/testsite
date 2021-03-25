from decimal import Decimal
from django.conf import settings
from blog.models import Post


class Cart(object):
    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # saving empty cart in sessions
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):

        product_ids = self.cart.keys()
        posts = Post.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for post in posts:
            cart[str(post.id)]['post'] = post

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # counting for each item in Cart
        return sum(item['quantity'] for item in self.cart.values())


    def add(self, post, quantity=1, update_quanity=False):
        # adding items in cart or refresh cart's data

        post_id = str(post.id)
        if post_id not in self.cart:
            self.cart[post_id] = {'quantity': 0, 'price': str(post.price)}

        if update_quanity:
            self.cart[post_id]['quantity'] = quantity
        else:
            self.cart[post_id]['quantity'] += quantity
        self.save()

    def save(self):
        #saving Items
        self.session.modified = True

    def remove(self, post):
        #removing item
        post_id = str(post.id)
        if post_id in self.cart:
            del self.cart[post_id]
            self.save()

    def get_total_price(self):
        # getting total price
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        #clearing cart in session
        del self.session[settings.CART_SESSION_ID]
        self.save()

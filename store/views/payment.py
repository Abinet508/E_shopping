from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Products
from store.models.orders import Order
from django.views import View


class payment (View):
   def post(self, request):
        merchantid = request.POST.get('merchantid')
        merchantOrderid = request.POST.get('merchantOrderid')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            
            payment = payment(merchantid=merchantid,
                              merchantOrderid=merchantOrderid,
                customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product.id)),
                          
                          )
            payment.save()
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')

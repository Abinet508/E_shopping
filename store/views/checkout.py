from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.payments import Payment
from store.models.product import Products
from store.models.orders import Order
import requests


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
           
            try:
                merchantid = request.POST.get('merchantid')
                merchantOrderid = request.POST.get('merchantOrderid')
                process="Expersess"
                susccessUrl="http://localhost:8081"
                cancelUrl="http://localhost:8081"
                
                experessAfter=24
                itemId=1
                itemName=product
                unitprice=product.price
                quantity=cart.get(str(product.id))
                discount=0.0
                handlingfee=0.0
                deliverfee=0.0
                tax1=0.0
                tax2=0.0
                obj={
                "process":process,
                "susccessUrl":susccessUrl,
                "cancelUrl":cancelUrl,
                "merchantid":merchantid,
                "merchantOrderid":merchantOrderid,
                "experessAfter":experessAfter,
                "itemId":itemId,
                "itemName":itemName,
                "unitprice":unitprice,
                "quantity":quantity,
                "discount":discount,
                "handlingfee":handlingfee,
                "deliverfee":deliverfee,
                "tax1":tax1,
                "tax2":tax2    
                }
                
                
                #print(cart.get(str(product.id)))
                red=requests.get("http://test.yenepay.com",obj)
                if red.status_code==200:
                    order = Order(customer=Customer(id=customer),
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)))
                    order.save()
                    payment = Payment(merchantid=merchantid,
                                        merchantOrderid=merchantOrderid,
                            customer=Customer(id=customer),
                                    product=product,
                                    price=product.price,
                                    quantity=cart.get(str(product.id)),
                                    
                                    )
                    payment.save()
                    request.session['cart'] = {}
                    return render(request,"payment.html",obj)
                else:      
                  request.session['cart'] = {}
                  return redirect('cart')
            except:
                if merchantid==None or merchantOrderid==None:
                    order = Order(customer=Customer(id=customer),
                                product=product,
                                price=product.price,
                                address=address,
                                phone=phone,
                                quantity=cart.get(str(product.id)))
                    order.save()
                request.session['cart'] = {}
                return redirect('cart')
                  
def success(request):
    return redirect('cart')
def cancel(request):
    return redirect('cart')                                                    
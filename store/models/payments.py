from django.db import models
from .product import Products
from .customer import Customer
from .orders import Order
import datetime

class Payment(models.Model):
    merchantid = models.CharField(max_length=50)
    merchantOrderid = models.CharField (max_length=50)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placePayment(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


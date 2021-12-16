from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.payments import Payment


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Payment)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'quantity', 'price', 'date', 'status','address')
    list_filter = ('status', 'customer', 'date', 'address')
    search_fields = ('customer',)
    raw_id_fields = ('customer',)
    date_hierarchy = 'date'
    ordering = ('status', 'date')
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'password')
    list_filter = ('first_name',)
    search_fields = ('first_name','phone','email')
    ordering = ('first_name',)    
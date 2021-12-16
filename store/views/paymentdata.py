from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Payment (View):
    def get(self, request):
        return render (request, 'signup.html')

    def payment(self, request):
        process="Expersess"
        susccessUrl="http://localhost:8081"
        cancelUrl="http://localhost:8081"
        merchantid='0999'
        merchantOrderid="val10.0"
        experessAfter=24
        itemId=1
        itemName="Payment"
        unitprice=15.0
        quantity=1
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
        
        
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        password = postData.get ('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        error_message = self.validateCustomer (customer)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password (customer.password)
            customer.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message

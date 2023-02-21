from itertools import product
from django.shortcuts import render,redirect
from django.http import HttpResponse
from customer.models import Mycart
from homecommon.models import Customer

from seller.models import Product

# Create your views here.
def cus_home(request):
    prod_list=Product.objects.all()
    return render(request,'cus_templates/cus_home.html',{'prod_data':prod_list})


def product_detail(request):
    return render(request,'cus_templates/product_detail.html')

def mycart(request):  
    if request.method=='POST':
          
        qty=request.POST['m_qty']
        new_cart=Mycart(
            # product_id= request.session['product'],
            # customer_id=request.session['customer'],
            quantity=qty,
          )
        new_cart.save()
    
    return render(request,'cus_templates/mycart.html')

def myorder(request):
    return render(request,'cus_templates/myorder.html')

def change_pass(request):
    return render(request,'cus_templates/change_pass.html')

def cus_profile(request):
    customer_details = Customer.objects.get(id = request.session['customer'])
    return render(request,'cus_templates/cus_profile.html',{'data':customer_details})

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('homecommon:home')
    
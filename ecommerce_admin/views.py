from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ad_login(request):
    return render(request,'admin_templates/ad_login.html')



def approve_seller(request):
    return render(request,'admin_templates/approve_seller.html')

def view_seller(request):
    return render(request,'admin_templates/view_seller.html')

def admin_home(request):
    return render(request,'admin_templates/admin_home.html')

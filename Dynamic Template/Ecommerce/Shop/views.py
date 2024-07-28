from django.shortcuts import render
from django.views import View
from.models import Product
from.forms import CustomRegestionForm

# Create your views here.
class ProductView(View):
     def get(self,request):
      gentspant=Product.objects.filter(category='GP')
      borkha=Product.objects.filter(category='BK')
      babyfashion=Product.objects.filter(category='BF')

       
      return render(request, 'Shop/home.html',{'gentspant':gentspant,'borkha':borkha,'babyfashion':babyfashion})

class Product_Detail(View):
 def get(self,request,pk):
  product=Product.objects.get(pk=pk)

  
  return render(request, 'Shop/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

def buy_now(request):
 return render(request, 'Shop/buynow.html')

def profile(request):
 return render(request, 'Shop/profile.html')

def address(request):
 return render(request, 'Shop/address.html')

def orders(request):
 return render(request, 'Shop/orders.html')

def change_password(request):
 return render(request, 'Shop/changepassword.html')

def lehenga(request,data = None):
 if data == None:
   lehenga = Product.objects.filter(category='L')
 elif data == 'luban' or data == 'infinity':
  lehenga =Product.objects.filter(category='L').filter(brand=data)
 elif data == 'below':
  lehenga=Product.objects.filter(category='L').filter(discount_gt =20000)
 elif data == 'above':
  lehenga=Product.objects.filter(category='L').filter(discount_lt =20000)
   
  return render(request, 'Shop/lehenga.html',{'lehenga':lehenga})

def login(request):
     return render(request, 'Shop/login.html')

class CustomerRegistration(View):
  def get(self,request):
   fm=CustomRegestionForm()
   return render(request, 'Shop/customerregistration.html',{'form':fm})
  
  def post(self,request):
    fm=CustomerRegistration()
    if fm.is_vaild():
      fm.save()
    return render(request, 'Shop/customerregistration.html',{'form':fm})


def checkout(request):
 return render(request, 'Shop/checkout.html')

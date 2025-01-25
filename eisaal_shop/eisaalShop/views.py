from django.shortcuts import render, redirect
from .models import addShopProducts, Orders, Contact_Us
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.contrib import messages


client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

# Create your views here.


def index(request):
    product = addShopProducts.objects.order_by('-Sno')[:3]
    params = {'product':product}
    return render(request, 'index.html', params)


def shop(request):
    allProducts = addShopProducts.objects.all()
    params = {'allProducts': allProducts}
    return render(request, 'products.html', params)


def get_products(request, Sno):
    getPro = addShopProducts.objects.filter(Sno = Sno)
    return render(request, 'get_products.html',{'getPro':getPro[0]})

def order(request, Sno):
    getOderDetails = addShopProducts.objects.filter(Sno = Sno)
    return render(request,"order.html", {'getOderDetails':getOderDetails[0]})

def order_now(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        product_name = request.POST.get('product_name')
        qut = int(request.POST.get('qut'))
        total_price = float(request.POST.get('total_price'))
        options = request.POST.get('options')
        
        if len(name) <= 3 or len(email) <= 5 or len(phone) < 10 or len(address) <= 8:
            messages.error(request, "invalid details please try again")
            return redirect('../')

        if options == "Online Payment":
            order_amount = int(total_price*100)
            order_currency = 'INR'
            order_receipt = f'receipt_{product_name}_{qut}'
            
            razorpay_order = client.order.create({
                "amount": order_amount,
                "currency": order_currency,
                "receipt": order_receipt,
                "payment_capture":1
            })
            
            context = {
                "razorpay_order_id": razorpay_order['id'],
                "razorpay_key_id": settings.RAZORPAY_KEY_ID,
                "amount": order_amount,
                "total_amount": total_price,
                "name": name,
                "email": email,
                "phone": phone,
                "address": address,
                "product_name": product_name,
                "qut": qut,
            }
            
            return render(request, 'order_now.html', context)
        else:
            cod_order = Orders(name=name, email=email, phone=phone, address=address, product_name=product_name, qut=qut,order_amount= total_price, options= options)
            cod_order.save()
            messages.success(request,"your order has been place successfully.")
            return redirect("/")


    return render(request, 'order_now.html')

@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        product_name = request.POST.get('product_name')
        qut = request.POST.get('qut')
        total_amount = request.POST.get('total_amount')
        
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
            'razorpay_signature': signature
        }
        print(params_dict)
        if params_dict != None:
            orders = Orders(name=name,email=email,phone=phone,address=address,qut=qut,product_name=product_name,order_amount=total_amount,razorpay_order_id=razorpay_order_id,razorpay_payment_id=razorpay_payment_id)
            orders.save()
            messages.success(request, "Your Order has been place successfully and your order id is:" + razorpay_order_id)
            return redirect('/')
        else:
            messages.error(request,"Something wants wrong, please try again")
            return redirect('/')
    return HttpResponseBadRequest('Invalid request method')
    
            
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        issue = request.POST.get('issue')
        if len(name) <=3:
            messages.error(request,"your name is not valid, please enter valid name.")
            return redirect("contact")
        if len(email) <=5:
            messages.error(request,"your email is not valid, please try again.")
            return redirect("contact")
        if len(phone) < 10:
            messages.error(request, "your phone no. is not valid, please try again.")
            return redirect("contact")
        if len(issue) <=5:
            messages.error(request, "please explain your issue in detailed.")
        
        else:
            contact = Contact_Us(name=name, email=email, phone=phone, issue=issue)
            contact.save()
            messages.success(request, "Your issue has been submitted successfully, we will be reach you shortly.")
            return redirect("contact")
    return render(request, "contact.html")
        
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
from django.shortcuts import render, redirect
from . models import Laptop, AddToCart, UserDetails, Payment
from django.http import JsonResponse, HttpRequest, HttpResponseRedirect
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
from .forms import UserDetailsForm
import razorpay
from django.conf import settings

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        totalitem = 0
        addtocart = AddToCart.objects.filter(user_id=request.user)
        sum = addtocart.aggregate(total = Sum('quantity'))
        totalitem  = sum['total']
        context = {
            'totalitem': totalitem
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

def laptop(request):
    if request.user.is_authenticated:
        totalitem = 0
        addtocart = AddToCart.objects.filter(user_id=request.user)
        sum = addtocart.aggregate(total = Sum('quantity'))
        totalitem  = sum['total']
        laptop = Laptop.objects.all()
        context = {
            'laptop': laptop,
            'totalitem': totalitem
        }
        return render(request, 'laptop.html', context)
    else:
        # return redirect('login')
        laptop = Laptop.objects.all()
        context = {
            'laptop': laptop,
        }
        return render(request, 'laptop.html', context)
    
def laptop_detail(request, pk):
    if request.user.is_authenticated:
        totalitem = 0  
        addtocart = AddToCart.objects.filter(user_id=request.user)
        sum = addtocart.aggregate(total = Sum('quantity'))
        totalitem  = sum['total']
        laptop = Laptop.objects.get(id=pk)
        context = {
            'laptop': laptop,
            'totalitem': totalitem
        }
        return render(request, 'laptop_details.html', context)
    else:
        laptop = Laptop.objects.get(id=pk)
        context = {
            'laptop': laptop,
        }
        return render(request, 'laptop_details.html', context)

def add_to_cart(request, pk):
    if request.user.is_authenticated:
        laptop = Laptop.objects.get(id=pk)
        if not AddToCart.objects.filter(laptop_id=pk, user_id=request.user).exists():
            AddToCart(laptop=laptop, user=request.user).save()
            return redirect('show_cart', )
        else:
            c = AddToCart.objects.get(laptop_id=pk, user_id=request.user)
            c.quantity += 1
            c.save()
            return redirect('show_cart')
    else:
        return redirect('login')    

def show_cart(request):
    if request.user.is_authenticated:
        totalitem = 0
        addtocart = AddToCart.objects.filter(user_id=request.user)
        sum = addtocart.aggregate(total = Sum('quantity'))
        totalitem  = sum['total']
        cart = AddToCart.objects.filter(user_id=request.user)
        total = 0
        for p in cart:
            value = p.quantity * p.laptop.price
            total = total + value
        context = {
            'cart': cart,
            'total': total,
            'totalitem': totalitem
        }
        return render(request, 'cart.html', context)
    else:
        return redirect('login')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = AddToCart.objects.get(laptop_id = prod_id, user_id=request.user)
        if c.quantity < 5:
            c.quantity += 1
            c.save()
            addtocart = AddToCart.objects.filter(user_id=request.user)
            sum = addtocart.aggregate(total = Sum('quantity'))
            totalitem  = sum['total']
            t = str(totalitem)
            cart = AddToCart.objects.filter(user_id=request.user)
            total = 0
            for p in cart:
                value = p.quantity * p.laptop.price
                total = total + value
            data={
                'quantity':c.quantity,
                'total': total,
                't': t
                }
            return JsonResponse(data)
        
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = AddToCart.objects.get(laptop_id = prod_id, user_id=request.user)
        if c.quantity >= 2:
            c.quantity -= 1
            c.save()
            addtocart = AddToCart.objects.filter(user_id=request.user)
            sum = addtocart.aggregate(total = Sum('quantity'))
            totalitem  = sum['total']
            t = str(totalitem)
            cart = AddToCart.objects.filter(user_id=request.user)
            total = 0
            for p in cart:
                value = p.quantity * p.laptop.price
                total = total + value
            data1={
                'quantity':c.quantity,
                'total': total,
                't': t
                }
            return JsonResponse(data1)
        
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = AddToCart.objects.get(laptop_id = prod_id, user_id=request.user)
        c.delete()
        addtocart = AddToCart.objects.filter(user_id=request.user)
        sum = addtocart.aggregate(total = Sum('quantity'))
        totalitem  = sum['total']
        if totalitem:
            t = str(totalitem)
        else:    
            t = "0"
        cart = AddToCart.objects.filter(user_id=request.user)
        total = 0
        for p in cart:
            value = p.quantity * p.laptop.price
            total = total + value
        data2={
            'total': total,
            't': t
            }
        return JsonResponse(data2)
    
def register_user(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully")
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lap')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def profile_user(request):
    default = {
        'user': '',
        'name': '',
        'email': '',
        'mobile': '',
        'housename': '',
        'area': '',
        'district': '',
        'state': '',
        'pin': ''
    }
    try:
        details = UserDetails.objects.get(user=request.user)
        form = UserDetailsForm(request.POST or None, instance=details)
    except Exception as e:
        print(e)
        form = UserDetailsForm(request.POST or None, initial=default) 
        
    if form.is_valid():
        form.save()
        return redirect('lap')
    else:
        print(form.errors)
    # form = UserDetails.objects.get(user_id=request.user)    
    addtocart = AddToCart.objects.filter(user_id=request.user)
    sum = addtocart.aggregate(total = Sum('quantity'))
    totalitem  = sum['total']    
    context = {
        'form': form,
        'totalitem': totalitem
    }
    return render(request, 'profile.html', context)

def order(request):
    cart = AddToCart.objects.filter(user_id=request.user)
    total = 0
    for p in cart:
        value = p.quantity * p.laptop.price
        total = total + value
    amount = int(total * 100)
    if amount > 0:
        client = razorpay.Client(auth=(settings.ID, settings.SECRET))
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        order_id = payment['id']
        order_status = payment['status']
        if order_status == 'created':
            paymentnew = Payment(user=request.user, amount=total, razorpay_order_id=order_id)
            paymentnew.save()
        
        # AddToCart(razor_pay_order_id=payment['id']).save()

        print('***')
        print(payment)
        print('***')

        details = UserDetails.objects.filter(user_id=request.user)
        print(details)
        totalitem = 0
        addtocart = AddToCart.objects.filter(user_id=request.user)
        sum = addtocart.aggregate(total = Sum('quantity'))
        totalitem  = sum['total']
        cart = AddToCart.objects.filter(user_id=request.user)
        total = 0
        for p in cart:
            value = p.quantity * p.laptop.price
            total = total + value
        context = {
            'details': details,
            'total': total,
            'payment': payment,
            'totalitem': totalitem
        }
        return render(request, 'order.html', context)
    else:
        # messages.info(request, 'Add items to cart before proceeding')    
        return render(request, 'cart.html')

def buynow(request, amt):
    total = amt
    amount = int(total * 100)
    if request.user.is_authenticated:
        client = razorpay.Client(auth=(settings.ID, settings.SECRET))
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        order_id = payment['id']
        order_status = payment['status']
        if order_status == 'created':
            paymentnew = Payment(user=request.user, amount=total, razorpay_order_id=order_id)
            paymentnew.save()
        
        # AddToCart(razor_pay_order_id=payment['id']).save()

        print('***')
        print(payment)
        print('***')

        details = UserDetails.objects.filter(user_id=request.user)
        print(details)
        totalitem = 0
        addtocart = AddToCart.objects.filter(user_id=request.user)
        sum = addtocart.aggregate(total = Sum('quantity'))
        totalitem  = sum['total']
        total = amt
        context = {
            'details': details,
            'total': total,
            'payment': payment,
            'totalitem': totalitem
        }
        return render(request, 'order.html', context)
    else:
        return redirect('login')
    
def success(request):
        order_id = request.GET.get('order_id')
        print(order_id)
        payment_id = request.GET.get('payment_id')
        print(payment_id)

        try:
            payment = Payment.objects.get(razorpay_order_id=order_id)
            payment.paid = True
            payment.razorpay_payment_id = payment_id
            payment.save()
        except Payment.DoesNotExist:
            payment = None    

        cart = AddToCart.objects.filter(user=request.user)
        cart.delete()
        
        return render(request, 'success.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from delivery.models import Customer, Restaurants, Menu, Cart
from delivery.form import ResForm, MenuForm
from django.conf import settings
from .models import Cart, CartItem, Menu, Customer, Order
import razorpay

# Create your views here.
def customer_home(request):
    return render(request,'delivery/customer_home.html')

def sign_in(request):
    return render(request, 'delivery/sign_in.html')

def sign_up(request):
    return render(request,'delivery/sign_up.html')

def admin_home(request):
    return render(request,'delivery/admin_home.html')


def handle_signin(request):
    li = Restaurants.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'Mealmate' and password == '20Meal@25':
            request.session["username"] = username 
            return render(request, 'delivery/admin_home.html', {'username': username})
        try:
            cus = Customer.objects.get(username=username, password=password)
            request.session["username"] = username
            return render(request, 'delivery/cusdisplay_res.html', {'li': li,'username': username})
        except:
            return render(request, 'delivery/failed.html')
    
def handle_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        try:
            cus = Customer.objects.get( username =  username, password = password)
        except:
            cus = Customer(username= username, password = password, email = email, mobile= mobile, address=address)
            cus.save()
        return render(request, 'delivery/sign_in.html')
    else:
        return HttpResponse('Invalid Request')

def add_res(request):
    if request.method == "POST":
        form = ResForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save()
            messages.success(request, "Restaurant info submitted successfully!")
            return redirect('delivery:admin_res')  # correct
    else:
        form = ResForm()

    return render(request, 'delivery/add_res.html', {'form': form})


def display_res(request):
    li = Restaurants.objects.all()
    return render(request, 'delivery/display_res.html',{'li':li})


def about(request):
    username = request.session.get('username', 'Guest')
    return render(request, 'delivery/about.html', {'username': username})

def admin_menu(request, id):
    res = Restaurants.objects.get(pk=id)
    menu = Menu.objects.filter(res=res)  
    return render(request, 'delivery/admin_menu.html',{'res':res, 'menu':menu, 'id':id})

def admin_res(request):
    li = Restaurants.objects.all()  
    return render(request, 'delivery/admin_res.html', {'li': li})

def add_menu(request, id):
    restaurant = Restaurants.objects.get(id=id)

    if request.method == "POST":
        item_name = request.POST.get("item_name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        is_available = request.POST.get("is_available") == "on"
        category = request.POST.get("category")
        img = request.POST.get("img")

        Menu.objects.create(
            res=restaurant,
            item_name=item_name,
            description=description,
            price=price,
            is_available=is_available,
            category=category,
            img=img
        )

        return redirect("delivery:admin_menu", id=id)

    return render(request, "delivery/add_menu.html", {
        "restaurant": restaurant
    })

def edit_menu(request, id):
    menu = Menu.objects.get(id=id)

    if request.method == "POST":
        menu.item_name = request.POST.get('item_name')
        menu.description = request.POST.get('description')
        menu.price = request.POST.get('price')

        if request.FILES.get('img'):
            menu.img = request.FILES['img']

        menu.is_available = request.POST.get('is_available') == "True"
        menu.save()

        return redirect('delivery:admin_menu', id=menu.res.id)

    return render(request, 'delivery/edit_menu.html', {'menu': menu})

def delete_menu(request, id):
    item = Menu.objects.get(id=id)
    restaurant_id = item.res.id
    
    if request.method == "POST":
        item.delete()
        return redirect('delivery:admin_menu', id=restaurant_id)

    return render(request, "delivery/delete_menu.html", {
        "item": item
    })

def delete_res(request, id):
    restaurant = get_object_or_404(Restaurants, id=id)

    if request.method == "POST":
        restaurant.delete()
        return redirect('delivery:admin_res')  

    return render(request, "delivery/delete_res.html", {
        "restaurant": restaurant
    })


def admin_users(request):
    users = Customer.objects.all()
    return render(request, "delivery/admin_users.html", {
        "users": users
    })

def edit_user(request, id):
    user = Customer.objects.get(id=id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.address = request.POST.get("address")
        user.save()

        return redirect("delivery:admin_users")

    return render(request, "delivery/edit_user.html", {"user": user})

def delete_user(request, id):
    user = Customer.objects.get(id=id)

    if request.method == "POST":
        user.delete()
        return redirect("delivery:admin_users")

    return render(request, "delivery/delete_user.html", {"user": user})


def cusdisplay_res(request, username):
    # ✅ Match session user with URL username
    session_user = request.session.get("username")
    if session_user != username:
        messages.error(request, "Unauthorized access.")
        return redirect("delivery:sign_in")
    
    # If authenticated → proceed
    customer = Customer.objects.get(username=username)
    li = Restaurants.objects.all()

    return render(request, "delivery/cusdisplay_res.html", {
        "li": li,
        "username": username
    })

def cusmenu(request,id, username):
    res = Restaurants.objects.get(pk=id)
    menu = Menu.objects.filter(res=res)  
    return render(request, 'delivery/cusmenu.html',{'res':res, 'menu':menu, 'username':username})


def show_cart(request, username):
    customer = Customer.objects.get(username=username)
    cart = Cart.objects.filter(customer=customer).first()

    if request.method == "POST":
        item_id = request.POST.get("item_id")
        quantity = request.POST.get("quantity")

        cart_item = CartItem.objects.get(id=item_id)
        cart_item.quantity = quantity
        cart_item.save()

        return redirect("delivery:show_cart", username=username)

    items = cart.items.all() if cart else []
    total_price = sum(item.total_price for item in items)

    return render(request, "delivery/show_cart.html", {
        "username": username,
        "cart": cart,
        "items": items,
        "total_price": total_price
    })

def add_to_cart(request, menuid, username):
    customer = Customer.objects.get(username=username)
    menu_item = Menu.objects.get(id=menuid)

    cart, created = Cart.objects.get_or_create(customer=customer)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        item=menu_item
    )

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    return redirect('delivery:show_cart', username=username)



def checkout(request, username):
    customer = Customer.objects.get(username=username)
    cart = Cart.objects.filter(customer=customer).first()
    cart_items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    if total_price == 0:
        return render(request, 'delivery/checkout.html', {
            'error': 'Your cart is Empty',
            'username': username
        })

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    order_data = {
        'amount': int(total_price * 100),
        'currency': 'INR',
        'payment_capture': '1',
    }

    razorpay_order = client.order.create(data=order_data)

    return render(request, 'delivery/checkout.html', {
        'username': username,
        'cart_items': cart_items,
        'total_price': total_price,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'order_id': razorpay_order['id'],
        'amount': total_price,
    })

def orders(request, username):
        customer = Customer.objects.get(username = username)
        cart = Cart.objects.filter(customer=customer).first()
        cart_items = cart.items.all() if cart else []
        total_price = cart.total_price() if cart else 0

        res = customer 
        
        if cart:
            cart.items.all().delete()

        return render(request, 'delivery/orders.html',{
        'username':username,
        'cart_items':cart_items,
        'total_price':total_price,
        'customer':customer,
        'res': res,
        })

def orders_list(request):
    orders = Order.objects.select_related("customer").prefetch_related("items__item")

    return render(request, "delivery/orders_list.html", {
        "orders": orders
    })

from .models import OrderItem
def save_order(request, username):
    customer = Customer.objects.get(username=username)
    cart = Cart.objects.filter(customer=customer).first()

    if not cart or cart.items.count() == 0:
        return redirect("delivery:orders", username=username)

    # Create Order
    order = Order.objects.create(
        customer=customer,
        total_amount=cart.total_price()
    )

    # Create OrderItems
    for c in cart.items.all():
        OrderItem.objects.create(
            order=order,
            item=c.item,
            quantity=c.quantity
        )

    # Clear cart
    cart.items.all().delete()

    return redirect("delivery:orders", username=username)

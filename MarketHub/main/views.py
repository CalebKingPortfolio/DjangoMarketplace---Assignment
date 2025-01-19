import sys
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import MessageForm, RegisterForm, ListingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Listing, Order, Messages
from django.contrib import messages

# View for the Home Page
def home(request):
    listings = Listing.objects.all() # Gathers the listings  
    return render(request, 'main/home.html', {"listings": listings}) # Returns the Home Page with the listing items

# View for sign up page
def register(request): 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
        else:
            return render(request, 'registration/register.html', {"form": form}) # Returns the register page and the reigster Form
    form = RegisterForm() # Loads the Register Form
    return render(request, 'registration/register.html', {"form": form}) # Returns the register page and the reigster Form

# View for the Create Listing Page
# Requires the user to be logged in before accessing redirects to login
@login_required(login_url="/login")
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = request.user
            listing.save()
            return redirect("/my-listing") # Returns to the My_listing page 
    else:
        form = ListingForm() # loads the form page 
        return render(request, 'my_account/create_listing.html', {"form": form}) # Returns the create listing page and the Listing Form

# View for the My Listing Page - DELETE LISTING
# Requires the user to be logged in before accessing redirects to login 
@login_required(login_url="/login")
def my_listings(request):
    listings = Listing.objects.all() 
    #Delete
    if request.method == "POST":
        listing_id = request.POST.get("listing-id")
        listing = Listing.objects.filter(id=listing_id).first()
        if listing and listing.author == request.user:
            listing.delete() # Deletes the listing
    return render(request, 'my_account/my_listing.html', {"listings": listings}) # Returns the user to my listing page and the Listing items


# View for the My Listing Edit Page
# Requires the user to be logged in before accessing redirects to login 
@login_required(login_url="/login")
def update_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if listing.author != request.user: #fix issue with who can edit the listing
        return HttpResponseForbidden("You are not allowed to edit this listing.")
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('/') 
    context = {'form' :form}
    return render(request, 'my_account/create_listing.html', {"form": form})


# View for searching for listings 
def list_listing(request):
    if request.method == "POST":
        searched = request.POST['searched']
        listings = Listing.objects.filter(title__contains=searched)
        return render(request, 'main/search_listing.html', {'searched': searched,'listings':listings})   
    else:
        return render(request, 'main/search_listing.html')
    

# View for Listing Item
# Requires the user to be logged in before accessing redirects to login 
@login_required(login_url="/login")
def listing_item(request,pk):
    listing = Listing.objects.get(id=pk) 
    order = Order()
    orders = Order.objects.filter(listing_id=listing, user_id=request.user)
    
    if orders.exists():
       order_exists = orders.exists()
       return render(request, 'main/listing_item.html', {"listing": listing, "order_exists": order_exists})
    
    if request.method == 'POST':
        order.listing_id = listing
        order.user_id = request.user
        order.save()
        return redirect(f'/listing-messages/{ order.id }')
    else:
        return render(request, 'main/listing_item.html', {"listing": listing})

        
# View for Listing messages
# Requires the user to be logged in before accessing redirects to login 
@login_required(login_url="/login")
def listing_messages(request,pk):   
    order = Order.objects.get(id=pk)   
    listing_user = order.listing_id.author
    messages = Messages.objects.filter(order_id=order)
    print("Order Listing ID:", listing_user)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.order_id = order
            message.listing_id = order.listing_id
            message.user_id = request.user
            message = form.save()
            return redirect(f'/listing-messages/{ pk }')
    else:
        form = MessageForm()
    return render(request, 'my_account/listing_messages.html', {"form": form, "messages": messages, "order": order })


# View for My Orders
# Requires the user to be logged in before accessing redirects to login 
@login_required(login_url="/login")
def my_orders(request):
    listings = Listing.objects.all()
    orders = Order.objects.all() 
    return render(request, 'my_account/my_order.html', {"orders": orders, "listings": listings})

# View for My Listing Querys
# Requires the user to be logged in before accessing redirects to login 
@login_required(login_url="/login")
def listing_querys(request, pk):
    listing = Listing.objects.get(id=pk)
    orders = Order.objects.all() 
    return render(request, 'my_account/listing_querys.html', {"orders": orders, "listing": listing})
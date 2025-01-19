from django.urls import path
from . import views 

urlpatterns = [
    
   path('', views.home, name='home'), # Home Page

   path('home', views.home, name='home'), # Home Page

   path('register', views.register, name='register'), # Register Page
   
   path('create-listing', views.create_listing, name='create-listing'), # Create Listing

   path('my-listing', views.my_listings, name='my_listings'), # My Listings

   path('update-listing/<str:pk>/', views.update_listing, name='update-listing'), # Edit Listing
   
   path('search-listing', views.list_listing, name='search-listing'),  # Search Listing

   path('listing-item/<int:pk>', views.listing_item, name='listing-item'), # Listing item

   path('listing-messages/<int:pk>', views.listing_messages, name='listing-messages'),    # Listing Message

   path('my-orders', views.my_orders, name='my-orders'), # My Orders

   path('listing-querys/<int:pk>', views.listing_querys, name='listing-querys'), # Listing Querys

]


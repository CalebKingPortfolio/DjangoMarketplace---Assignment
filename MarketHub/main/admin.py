from django.contrib import admin
from .models import Listing, Order, Messages

admin.site.register(Listing)
admin.site.register(Order)
admin.site.register(Messages)

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



class Listing(models.Model):
 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    description =  models.TextField()
    type = models.CharField(default='Other', max_length=255)
    location = models.CharField(max_length=255)
    status = models.TextField(default='Selling')
    created_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=7))
    image = models.ImageField(upload_to='listing_images/')
    


class Order(models.Model):

    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

class Messages(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


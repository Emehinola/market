from django.db import models
from user.models import User

# Create your models here.

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = [
        ("accessory", "Accessory"),
        ("computer", "Computer"),
        ("electronic", "Electronic"),
        ("fashion", "Fashion"),
        ("phones", "Phone")
    ]
    state_category = [
        ('used', 'Used'),
        ('new', 'New')
    ]

    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=50)            
    category = models.CharField(max_length=30, choices=categories)
    price = models.IntegerField(blank=True)
    location = models.CharField(max_length=200)
    product_state = models.CharField(max_length=5, choices=state_category)
    image1 = models.ImageField(upload_to="product images")
    image2 = models.ImageField(upload_to="product images")
    image3 = models.ImageField(upload_to="product images")
    description = models.TextField()
    delivery_description = models.TextField(null=True)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = "Product"

    def __str__(self):
        return self.name            
    

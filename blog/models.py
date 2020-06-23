from django.db import models
from user.models import User
from django.shortcuts import reverse

# Create your models here.

#  blog model
class Blog(models.Model):
    title = models.CharField(max_length=500, blank=False)
    content = models.TextField()
    image = models.ImageField(upload_to='blog images')
    author = models.CharField(max_length=50)
    categories = [
        ("sport", "Sport"),
        ("religion","Religion"),
        ("technology","Technology"),
        ("politics","Politics"),
        ("education", "Education")
         ]
    category = models.CharField(choices=categories, max_length=30)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Blogs"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=20)
    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()  
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ['-created_at']

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
      
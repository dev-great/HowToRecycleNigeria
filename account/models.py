from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class BecomeAnAgent(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=30)
    state = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    
class ServiceModel(models.Model):
    name = models.CharField(max_length=400)
    details = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
 
    
class CollectionCenterModel(models.Model):
    name = models.CharField(max_length=400)
    number = models.CharField(max_length=15)
    whats_app = models.CharField(max_length=15)
    state = models.CharField(max_length=400)
    google_map_link = models.CharField(max_length=4000, blank=True, null=True)
    full_address = models.TextField()
    opening_time = models.CharField(max_length=15)
    closing_time = models.CharField(max_length=15)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    

class BlogModel(models.Model):
    title= models.CharField(max_length=200)
    image = CloudinaryField('image')
    content= models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    
class NewslettersModel(models.Model):
    name = models.CharField(max_length=400) 
    email = models.EmailField(unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    
class ContaclFormModel(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(unique=False)
    phone = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
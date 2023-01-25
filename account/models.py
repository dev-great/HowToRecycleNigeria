from django.db import models

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
    image = models.ImageField(upload_to='images/')
    details = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
 
 
class PricesModel(models.Model):
    name = models.CharField(max_length=400)
    price = models.CharField(max_length=2000)
        
    
    
class CollectionCenterModel(models.Model):
    name = models.CharField(max_length=400)
    number = models.CharField(max_length=15)
    whats_app = models.CharField(max_length=15)
    state = models.CharField(max_length=400)
    google_map_link = models.CharField(max_length=4000)
    full_address = models.TextField()
    opening_time = models.CharField(max_length=15)
    closing_time = models.CharField(max_length=15)
    pricing = models.ForeignKey(PricesModel, on_delete=models.CASCADE, )
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    

class BlogModel(models.Model):
    title= models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    content= models.TextField()
    pub_date = models.DateTimeField('date published')
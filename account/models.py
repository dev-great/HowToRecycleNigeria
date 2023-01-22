from django.db import models



STATUS = (
    (0,"Pending"),
    (1,"Accepted"),
    (2,"Closed")
)
# Create your models here.
class BecomeAnAgent(models.Model):
    name = models.CharField(max_length=400)
    slug = models.SlugField(max_length=200, unique=True)
    phoneNumber = models.CharField(max_length=30)
    state = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    
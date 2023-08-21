from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomerUser(AbstractUser):
    username = None
    email = models.EmailField( unique=True)  
    address = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'address'
    ]


    def __str__(self):
        return self.email
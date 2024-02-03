from django.db import models

# Create your models here.
from django.db import models

# # Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)#2023-08-04 13:22:28.164297
    def __str__(self):
        return self.name

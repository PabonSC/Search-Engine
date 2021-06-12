from django.db import models

# Create your models here.

class login(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
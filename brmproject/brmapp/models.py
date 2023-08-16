

# Create your models here.

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)



#return the book name which we put
    def __str__(self):
        return self.title
    

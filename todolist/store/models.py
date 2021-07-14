from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_length=10,max_digits=10,decimal_places=2)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
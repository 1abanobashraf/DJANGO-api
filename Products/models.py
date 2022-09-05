
from django.db import models


class Categore(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return f'{self.name} ({self.description})'
    
class Brand(models.Model):
    manufactorerName = models.CharField(max_length=200)
    manufactorerBrnad = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.manufactorerName} ({self.manufactorerBrnad})'

class Product(models.Model):
    name = models.CharField(max_length=200)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)
    categore = models.ForeignKey(Categore, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.description
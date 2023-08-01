from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

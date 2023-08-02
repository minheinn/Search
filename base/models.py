from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, blank=True, editable=False)

    def __str__(self):
        return self.name

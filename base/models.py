from django.db import models
from autoslug import AutoSlugField
from django.utils.crypto import get_random_string

# Create your models here.
def unique_slugify(instance, slug):
        model = instance.__class__
        unique_slug = slug
        while model.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + get_random_string(length=4)
        return unique_slug

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='photos/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True, blank=True, editable=False)

    def __str__(self):
        return self.name

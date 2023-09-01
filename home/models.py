from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)
    logo = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    rank = models.IntegerField()
    url = models.URLField(blank=True, max_length=500)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()

    def __str__(self):
        return self.name

STOCK = (('in_stock', 'In Stock'),('out of stock', 'Out of stock'))
LABELS = (('','default'),('new', 'New'),('sale', 'Sale'),('hot', 'Hot'))
class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    stock = models.CharField(choices=STOCK, max_length=50)
    label = models.CharField(choices=LABELS, max_length=50, blank=True)

    def __str__(self):
        return self.name

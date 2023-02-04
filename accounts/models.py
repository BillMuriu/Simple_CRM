from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
























class Cpu(models.Model):
    family = models.CharField(max_length=200, null=True)
    model = models.CharField(max_length=200, null=True)
    socket = models.CharField(max_length=200, null=True)
    # clock_speed = models.CharField(max_length=200, null=True)
    # cores = models.CharField(max_length=200, null=True)
    # threads = models.CharField(max_length=200, null=True)
    # cache = models.CharField(max_length=200, null=True)
    # tdp = models.CharField(max_length=200, null=True)
    # integrated_graphics = models.CharField(max_length=200, null=True)
    # lithography = models.CharField(max_length=200, null=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.family



    
class Motherboard(models.Model):
    chipset = models.CharField(max_length=200, null=True)
    socket = models.CharField(max_length=200, null=True)
    # form_factor = models.CharField(max_length=200, null=True)
    # memory_type = models.CharField(max_length=200, null=True)
    # memory_slots = models.CharField(max_length=200, null=True)
    # max_memory = models.CharField(max_length=200, null=True)
    # memory_speed = models.CharField(max_length=200, null=True)
    # storage = models.CharField(max_length=200, null=True)
    # graphics = models.CharField(max_length=200, null=True)
    # audio = models.CharField(max_length=200, null=True)
    # lan = models.CharField(max_length=200, null=True)
    # usb = models.CharField(max_length=200, null=True)
    # sata = models.CharField(max_length=200, null=True)
    # date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.chipset































class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag) # Many to many relationship

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name
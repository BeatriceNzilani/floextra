from django.db import models
# models.py

from django.utils.html import format_html

class NavigationLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=1024)

    def __str__(self):
        return self.title

    def display_url(self):
        return format_html('<a href="{}" target="_blank">{}</a>', self.url, self.url)
    display_url.short_description = 'URL' 


class User(models.Model):
    name = models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Bookings(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    date = models.DateTimeField()
    design_type =models.CharField(max_length=50)
    budget = models.CharField(max_length=50)
    color_preference=models.CharField(max_length=50)
    furniture_needs=models.CharField(max_length=50)
    flooring_preference=models.CharField(max_length=50)
    timeline=models.CharField(max_length=50)
    comments=models.TextField()

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')  
    title = models.CharField(max_length=50)        

    def __str__(self):
        return self.title
    
class contactinfo(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)  
    transaction_date = models.DateTimeField()
    account_reference = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_id} - {self.status}"

    





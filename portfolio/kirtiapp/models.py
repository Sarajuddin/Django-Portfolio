from django.db import models

# Create your models here.
class Connection(models.Model):
    name = models.CharField(max_length=100, default='', null=True)
    email = models.EmailField(max_length=100, default='', null=True)
    phone = models.CharField(max_length=50, default='', null=True)
    message = models.TextField(max_length=1000, default='', null=True)

    time = models.CharField(max_length=150, default='', null=True)
    device_type = models.CharField(max_length=250, default='', null=True)
    os = models.CharField(max_length=50, default='', null=True)
    browser = models.CharField(max_length=50, default='', null=True)
    ip = models.CharField(max_length=50, default='', null=True)
    location = models.CharField(max_length=500, default='', null=True)
    latitude = models.CharField(max_length=50, default='', null=True)
    longitude = models.CharField(max_length=50, default='', null=True)
    def __str__(self):
        return f"{self.name} / {self.email} / {self.phone} / {self.ip}"

class Viewed(models.Model):
    time = models.CharField(max_length=150, default='', null=True)
    device_type = models.CharField(max_length=250, default='', null=True)
    os = models.CharField(max_length=50, default='', null=True)
    browser = models.CharField(max_length=50, default='', null=True)
    
    def __str__(self):
        return f"{self.device_type} / {self.browser} / {self.os} / {self.time}"
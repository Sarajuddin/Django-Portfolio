from django.db import models

# Create your models here.
class Connection(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)

    hostname = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    time = models.CharField(max_length=150)
    def __str__(self):
        return f"{self.name} / {self.email} / {self.phone} / {self.ip}"

class viewed(models.Model):
    hostname = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    time = models.CharField(max_length=150)
    def __str__(self):
        return f"{self.ip} / {self.hostname} / {self.browser} / {self.os}"

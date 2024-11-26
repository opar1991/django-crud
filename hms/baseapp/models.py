from django.db import models

# Create your models here.
class Members(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    County = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


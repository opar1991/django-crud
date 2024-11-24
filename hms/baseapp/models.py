from django.db import models

# Create your models here.
class Rooms(models.Model):
    #host = 
    #tpoic=
    name = models.CharField(max_length=200)
    decription = models.TextField(null=True, blank=True)
   # participants = models.
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

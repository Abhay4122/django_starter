from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null=True)
    doj = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
